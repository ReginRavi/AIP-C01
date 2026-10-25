"""
Vault Transit Auto-Unseal Verification & Demonstration Script
"""
import json
import time
import urllib.request
import urllib.error
import subprocess
import os
import sys

TARGET_ADDR = "http://127.0.0.1:8220"
TRANSIT_ADDR = "http://127.0.0.1:8100"
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target_vault_keys.json")

def api_call(url: str, method: str = "GET", data: dict = None, token: str = None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["X-Vault-Token"] = token
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8")
            return json.loads(content) if content else {}
    except urllib.error.HTTPError as e:
        content = e.read().decode("utf-8")
        try:
            return json.loads(content)
        except Exception:
            raise Exception(f"HTTP {e.code}: {content}")

def check_seal_status():
    res = api_call(f"{TARGET_ADDR}/v1/sys/seal-status")
    return res

def main():
    print("=" * 65)
    print("  HashiCorp Vault: Transit Auto-Unseal Test & Demonstration")
    print("=" * 65)

    # 1. Verify Transit Vault KMS is healthy
    print("\n[Step 1] Checking Transit KMS Vault (Port 8100)...")
    try:
        transit_health = api_call(f"{TRANSIT_ADDR}/v1/sys/health")
        print(f"  [OK] Transit KMS Vault is online: Version={transit_health.get('version')}, Sealed={transit_health.get('sealed')}")
    except Exception as e:
        print(f"  [ERROR] Transit KMS Vault is not reachable at {TRANSIT_ADDR}: {e}")
        sys.exit(1)

    # 2. Check Target Vault initialization state
    print("\n[Step 2] Checking Target Vault (Port 8220)...")
    seal_status = check_seal_status()
    is_init = seal_status.get("initialized", False)
    root_token = None

    if not is_init:
        print("  Target Vault is NOT initialized yet.")
        print("  Initializing Target Vault with Transit Auto-Unseal...")
        init_payload = {
            "recovery_shares": 1,
            "recovery_threshold": 1
        }
        init_res = api_call(f"{TARGET_ADDR}/v1/sys/init", method="POST", data=init_payload)
        
        root_token = init_res.get("root_token")
        recovery_keys = init_res.get("recovery_keys", [])
        
        print("\n  =======================================================")
        print("  CRITICAL AUTO-UNSEAL BEHAVIOR OBSERVED:")
        print("  Notice that Vault returned RECOVERY KEYS, not Unseal Keys!")
        print(f"  - Recovery Key 1 : {recovery_keys[0] if recovery_keys else 'N/A'}")
        print(f"  - Root Token     : {root_token}")
        print("  =======================================================\n")

        with open(STATE_FILE, "w") as f:
            json.dump({"root_token": root_token, "recovery_keys": recovery_keys}, f, indent=2)
        print(f"  Credentials saved locally to: {STATE_FILE}")
        time.sleep(2)
    else:
        print("  Target Vault is already initialized.")
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r") as f:
                saved = json.load(f)
                root_token = saved.get("root_token")
        else:
            print("  Note: No saved root_token found in target_vault_keys.json.")

    # 3. Check seal status
    status = check_seal_status()
    print(f"\n[Step 3] Current Target Vault State:")
    print(f"  - Initialized   : {status.get('initialized')}")
    print(f"  - Sealed        : {status.get('sealed')}")
    print(f"  - Type          : {status.get('type')} (transit)")
    print(f"  - Recovery Mode : {status.get('recovery_seal', False)}")

    # 4. Enable KV and write test secret
    if root_token:
        print("\n[Step 4] Writing sample secret into Target Vault...")
        try:
            api_call(f"{TARGET_ADDR}/v1/sys/mounts/secret", method="POST", 
                     data={"type": "kv", "options": {"version": "2"}}, token=root_token)
        except Exception:
            pass  # Mount may already exist

        secret_path = "secret/data/transit-autounseal-test"
        payload = {
            "data": {
                "message": "Transit Auto-Unseal successfully decrypted this!",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        }
        api_call(f"{TARGET_ADDR}/v1/{secret_path}", method="POST", data=payload, token=root_token)
        print(f"  [OK] Secret saved to '{secret_path}'")

    # 5. Restart Target Vault to prove Auto-Unseal
    print("\n[Step 5] Restarting Target Vault container ('vault-target-unsealed')...")
    restart_res = subprocess.run(["docker", "restart", "vault-target-unsealed"], capture_output=True, text=True)
    if restart_res.returncode != 0:
        print(f"  [WARN] Failed to restart container: {restart_res.stderr}")
    else:
        print("  Container restarted.")

    print("  Waiting 4 seconds for Target Vault to boot and contact Transit KMS...")
    time.sleep(4)

    # 6. Verify Auto-Unseal happened automatically!
    print("\n[Step 6] Verifying Auto-Unseal status after reboot...")
    new_status = check_seal_status()
    is_sealed = new_status.get("sealed", True)
    print(f"  - Sealed Status: {is_sealed}")

    if not is_sealed:
        print("\n" + "*" * 65)
        print("  SUCCESS! Target Vault AUTO-UNSEALED ITSELF without any human key!")
        print("*" * 65)
        if root_token:
            read_sec = api_call(f"{TARGET_ADDR}/v1/secret/data/transit-autounseal-test", token=root_token)
            sec_data = read_sec.get("data", {}).get("data", {})
            print(f"\n  Retrieved secret immediately after restart:")
            print(f"  - message   : {sec_data.get('message')}")
            print(f"  - timestamp : {sec_data.get('timestamp')}")
    else:
        print("\n  [FAIL] Target Vault is still sealed.")

if __name__ == "__main__":
    main()
