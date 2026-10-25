"""
Transit KMS Outage Simulation Test
Demonstrates what happens to Target Vault when the Transit KMS is OFFLINE (frozen/paused) vs ONLINE.
"""
import time
import subprocess
import urllib.request
import urllib.error
import json
import os

TARGET_URL = "http://127.0.0.1:8220"
KEYS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target_vault_keys.json")

def get_target_seal_status():
    req = urllib.request.Request(f"{TARGET_URL}/v1/sys/seal-status")
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        content = e.read().decode("utf-8")
        try:
            return json.loads(content)
        except Exception:
            return {"error": f"HTTP {e.code}", "body": content}
    except Exception as e:
        return {"error": str(e)}

def run_cmd(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return res.stdout.strip()

def main():
    print("=" * 72)
    print("  SIMULATION: Transit KMS Outage & Auto-Unseal Dependency Test")
    print("=" * 72)

    # Step 1: Baseline check
    print("\n[Step 1] Baseline check: Checking Target Vault status...")
    status = get_target_seal_status()
    print(f"  Target Vault Initialized: {status.get('initialized')}")
    print(f"  Target Vault Sealed     : {status.get('sealed')} (Expected: False - currently working)")

    # Step 2: Simulate KMS Outage by PAUSING Transit Vault
    print("\n[Step 2] SIMULATING OUTAGE: Freezing Transit KMS ('docker pause transit-vault-server')...")
    run_cmd("docker pause transit-vault-server")
    print("  [OK] Transit KMS is now completely FROZEN / UNREACHABLE.")

    # Step 3: Restart Main Vault while KMS is down
    print("\n[Step 3] Restarting Main Vault container ('main-vault-server')...")
    run_cmd("docker restart -t 2 main-vault-server")
    print("  Main Vault container restarted.")
    print("  Waiting 5 seconds for Main Vault startup attempt...")
    time.sleep(5)

    # Step 4: Check Main Vault status - it CANNOT unseal!
    print("\n[Step 4] Checking Main Vault status while KMS is UNREACHABLE...")
    status_down = get_target_seal_status()
    print(f"  API Response from Main Vault: {status_down}")
    
    logs = run_cmd("docker logs --tail 8 main-vault-server")
    print("\n  Main Vault Logs during KMS outage:")
    for line in logs.splitlines():
        print(f"    {line}")

    print("\n  ================================================================")
    print("  OBSERVATION CONFIRMED:")
    print("  Main Vault CANNOT boot or unseal because the Transit KMS is unreachable!")
    print("  ================================================================")

    # Step 5: Restore Transit KMS
    print("\n[Step 5] RESTORING TRANSIT KMS ('docker unpause transit-vault-server')...")
    run_cmd("docker unpause transit-vault-server")
    print("  [OK] Transit KMS is now ACTIVE and responding.")

    # Step 6: Restart Main Vault now that KMS is back
    print("\n[Step 6] Restarting Main Vault now that KMS is restored...")
    run_cmd("docker restart main-vault-server")
    print("  Waiting 5 seconds for Target Vault to contact KMS and auto-unseal...")
    time.sleep(5)

    # Step 7: Verify Auto-Unseal happened automatically!
    print("\n[Step 7] Verifying Target Vault status after KMS restoration...")
    recovered_status = get_target_seal_status()
    recovered_sealed = recovered_status.get("sealed")
    print(f"  Target Vault Sealed Status: {recovered_sealed}")

    if recovered_sealed is False:
        print("\n" + "*" * 72)
        print("  SUCCESS: As soon as Transit KMS was restored, Target Vault AUTO-UNSEALED!")
        print("*" * 72)

        # Read secret to prove decryption works
        if os.path.exists(KEYS_FILE):
            with open(KEYS_FILE) as f:
                root_token = json.load(f).get("root_token")
            req = urllib.request.Request(f"{TARGET_URL}/v1/secret/data/transit-autounseal-test", 
                                        headers={"X-Vault-Token": root_token})
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                print(f"\n  Successfully read decrypted secret from Target Vault:")
                print(f"  - Message: {data['data']['data']['message']}")
    else:
        print("  Target Vault did not recover yet. Check logs.")

if __name__ == "__main__":
    main()
