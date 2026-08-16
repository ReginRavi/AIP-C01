
### 1. Inbound vs. Outbound Rules (Core Concepts)

- **Inbound Rules:** Filter incoming traffic trying to reach your resource. <mark style="background:#fff88f">By default in AWS</mark>, **all <mark style="background:#fff88f">incoming traffic is blocked**</mark> unless explicitly allowed by a rule.

- **Outbound Rules:** Filter outgoing traffic initiated by your resource.<mark style="background:#fff88f"> By default in AWS</mark>, **all <mark style="background:#fff88f">outbound traffic is allowed**</mark> (`0.0.0.0/0` on all ports/protocols).

- **Stateful Nature of Security Groups:** If you allow inbound traffic on a port (e.g., port `443`), the response traffic back to the client is **automatically permitted** outbound, regardless of your outbound rule configuration.

### 2. Configuration Matrix for EC2 App Server + MySQL DB

To connect an EC2 application server to a MySQL database (Amazon RDS or an EC2 instance hosting MySQL), you create **two separate Security Groups**.

```
  [ Internet / User / Admin ]
               │
               ▼ (Port 443 / Port 22)
    ┌─────────────────────────────────┐
    │     EC2 App Security Group      │
    │        (sg-appserver)           │
    └────────────────┬────────────────┘
                     │
                     ▼ (Port 3306 - Source: sg-appserver)
    ┌─────────────────────────────────┐
    │     MySQL DB Security Group     │
    │          (sg-mysqldb)           │
    └─────────────────────────────────┘
```

#### A. EC2 App Server Security Group (`sg-appserver`)

|**Rule Type**|**Protocol**|**Port**|**Source / Destination**|**Purpose / Description**|
|---|---|---|---|---|
|**Inbound**|TCP|`443` (HTTPS)|`0.0.0.0/0` (or ALB Security Group)|End-user web traffic|
|**Inbound**|TCP|`80` (HTTP)|`0.0.0.0/0` (or ALB Security Group)|Web traffic / HTTP-to-HTTPS redirect|
|**Inbound**|TCP|`22` (SSH)|`Your-Corp-IP/32` or Bastion SG|Administrative shell access|
|**Outbound**|All|All|`0.0.0.0/0`|Outbound OS patching, external API calls, DB calls|

_(Optional Outbound Hardening: Restrict outbound TCP `3306` to target `sg-mysqldb` and TCP `443`/`80` for updates)._

#### B. MySQL Database Security Group (`sg-mysqldb`)

|**Rule Type**|**Protocol**|**Port**|**Source / Destination**|**Purpose / Description**|
|---|---|---|---|---|
|**Inbound**|TCP|`3306` (MySQL)|**`sg-appserver` (Security Group ID)**|**Only allows connections originating from the App Server SG**|
|**Inbound**|TCP|`3306` (MySQL)|_`sg-bastion`_ _(Optional)_|For DB administrators connecting via a bastion/jump host|
|**Outbound**|All / None|All|Default is fine; DB rarely initiates outbound|Responses to queries exit automatically (stateful)|

### 3. What to Configure First (Step-by-Step Order)

To avoid circular dependency or configuration errors, build in this sequence:

```
Step 1: Create sg-appserver (Leave DB rules aside, add HTTP/HTTPS/SSH)
   │
   ▼
Step 2: Create sg-mysqldb (Add Inbound Port 3306 -> Reference sg-appserver ID)
   │
   ▼
Step 3: Launch/Attach to EC2 App Server & MySQL Database
```

1. **Create the EC2 App Security Group (`sg-appserver`) first:** Add your inbound HTTP/HTTPS and restricted SSH rules.

2. **Create the Database Security Group (`sg-mysqldb`) second:** In the inbound rule for port `3306`, select **Custom** and enter the **ID of the app security group** (`sg-appserver`) as the source.

3. **Launch/Associate:** Attach `sg-appserver` to your EC2 instance and `sg-mysqldb` to your RDS instance or DB EC2.

### 4. Critical Watch-Outs & Anti-Patterns

- **Never Use `0.0.0.0/0` for MySQL (Port 3306):**

    - _Watch-out:_ Exposing port `3306` to the public internet leaves the database vulnerable to brute-force and credential-stuffing attacks.

    - _Fix:_ Always restrict the source to the App Server's Security Group ID (`sg-xxxx`) or a private subnet CIDR.

- **Reference Security Group IDs, Not Private IP Addresses:**
    
    - _Watch-out:_ If your EC2 app instances are managed by an **Auto Scaling Group (ASG)**, instances are terminated and created dynamically with changing private IPs.

    - _Fix:_ Sourcing the rule by `sg-appserver` automatically permits any new EC2 instance launched with that security group to connect without manual IP updates.

- **Subnet Routing & NACL Clashes (Network Access Control Lists):**
    
    - _Watch-out:_ <mark style="background:#fff88f">Security groups are **stateful**, but VPC NACLs are **stateless**</mark>. If your subnets use custom NACLs and you block ephemeral ports (`1024-65535`), the return traffic will fail even if the Security Group allows it.

    - _Fix:_ Ensure NACLs covering the DB subnet allow inbound `3306` and outbound ephemeral return ports.

- **MySQL `bind-address` Configuration (If Self-Hosting MySQL on EC2):**

    - _Watch-out:_ By default, MySQL server config (`/etc/mysql/mysql.conf.d/mysqld.cnf`) binds to `127.0.0.1` (localhost only). Even with open security groups, external app servers will get `Connection refused`.

    - _Fix:_ Update `bind-address` to `0.0.0.0` or the instance's private IP, and grant database user permissions using `'username'@'10.0.%.%'` or `'username'@'%'`.

- **Public Accessibility on RDS:**

    - _Watch-out:_ Setting `Publicly Accessible = Yes` on RDS provisions a public IP address on the database endpoint.

    - _Fix:_ Always set `Publicly Accessible = No` and place the database in **Private Subnets** with route tables that do not have an Internet Gateway (`igw-xxxx`) route.

**Create an outbound rule in the security group for the EC2 instance app servers using TCP protocol on port 3306. Set the destination as the security group for the MySQL DB servers**

**Create an inbound rule in the security group for the MySQL DB servers using TCP protocol on port 3306. Set the source as the security group for the EC2 instance app servers**

A security group controls the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance. Security groups are stateful. For example, if you send a request from an instance, the response traffic for that request is allowed to reach the instance regardless of the inbound security group rules. Responses to allowed inbound traffic are allowed to leave the instance, regardless of the outbound rules.

When you first create a security group, it has no inbound rules. Therefore, no inbound traffic is allowed until you add inbound rules to the security group. When you first create a security group, it has an outbound rule that allows all outbound traffic from the resource. You can remove the rule and add outbound rules that allow specific outbound traffic only. If your security group has no outbound rules, no outbound traffic is allowed.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q1-i1.jpg)

 via - [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

For the given use case, you need to set up an outbound rule in the security group for the EC2 instance app servers using TCP protocol on port 3306 and then select the destination as the security group for the MySQL DB servers. Further, you need to set up an inbound rule in the security group for the MySQL DB servers using TCP protocol on port 3306 and then select the source as the security group for the EC2 instance app servers. This combination would let the request be initiated from the EC2 instances and allowed into the DB servers. Since the security groups are stateful, the response from the DB servers would be allowed out of the DB servers (even though no outbound rules are configured in the DB security group) and further into the EC2 instances (even though no inbound rules are configured in the EC2 instance security group)

you need to set up an outbound rule in the security group for the EC2 instance app servers using TCP protocol on port 3306 and NOT on the ephemeral port range because the MySQL DB is configured to process requests on port 3306. A common use-case for ephemeral ports: these are used in NACLs to handle response traffic. Consider a custom network ACL for a VPC that supports IPv4 only. It includes rules that allow HTTP and HTTPS traffic in (inbound rules 100 and 110). There's a corresponding outbound rule that enables responses to that inbound traffic (outbound rule 140, which covers ephemeral ports 32768-65535). 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q1-i2.jpg)

 via - [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-ports](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-ports)