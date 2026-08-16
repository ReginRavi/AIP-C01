**Amazon Elastic Load Balancing (ELB)** is a fully managed AWS service that automatically distributes incoming application traffic across multiple backend targets. These targets can include Amazon EC2 instances, containers (Amazon ECS/EKS), IP addresses, and AWS Lambda functions.

ELB acts as the single point of contact for clients, improving an application’s **availability, scalability, and fault tolerance** by ensuring no single server is overloaded or becomes a single point of failure.

### Core Types of Elastic Load Balancers

AWS offers specialized load balancers depending on the OSI layer, protocol, and use case:

|**Load Balancer Type**|**Layer**|**Best For / Key Protocols**|**Key Features**|
|---|---|---|---|
|**Application Load Balancer (ALB)**|Layer 7 (Application)|HTTP, HTTPS, gRPC, WebSockets|Advanced routing (path-based, host-based, query parameter), microservices, containers, AWS Lambda integration, AWS WAF support.|
|**Network Load Balancer (NLB)**|Layer 4 (Transport)|TCP, UDP, TLS|Ultra-low latency, extreme performance (millions of requests/sec), static/Elastic IP per subnet, client source IP preservation.|
|**Gateway Load Balancer (GWLB)**|Layer 3 / 4|Third-party virtual appliances|Deploying and scaling firewalls, intrusion detection/prevention systems (IDS/IPS), and deep packet inspection appliances.|
|**Classic Load Balancer (CLB)** _(Legacy)_|Layer 4 / 7|Older EC2-Classic networks|Previous-generation load balancer, generally not recommended for new architectures.|

### Key Features and Benefits

1. **High Availability & Cross-Zone Balancing:**
    
    - ELB distributes traffic across targets in multiple AWS Availability Zones (AZs).

    - If an entire AZ experiences issues, ELB seamlessly reroutes traffic to healthy AZs.

2. **Automatic Scaling:**
    
    - ELB scales its own request-handling capacity up or down automatically based on traffic fluctuations without manual intervention.

    - Integrates tightly with **EC2 Auto Scaling** to automatically register new compute instances when demand rises and deregister them when traffic drops.

3. **Continuous Health Checks:**
    
    - Regularly monitors the health of registered targets.

    - If a server fails or becomes unresponsive, ELB stops sending requests to it until it passes health checks again.

4. **Security & SSL/TLS Offloading:**

    - Handles SSL/TLS certificate management and encryption/decryption at the load balancer level, freeing backend servers from CPU-heavy cryptographic tasks.

    - Integrates with **AWS Certificate Manager (ACM)**, **AWS WAF (Web Application Firewall)**, and **Amazon VPC Security Groups**.

5. **Monitoring & Logging:**

    - Integrates with **Amazon CloudWatch** for real-time metrics (latency, request count, error rates) and provides detailed **Access Logs** stored in Amazon S3 for compliance and troubleshooting.


### Core Concepts to Know

- **Listeners:** A process configured on the ELB that checks for connection requests based on the protocol and port you define (e.g., HTTPS on port 443).

- **Rules:** Conditions (e.g., request path `/api/*` or host header `app.example.com`) that determine where a listener routes traffic (mainly for ALB).

- **Target Groups:** Logical groupings of resources (EC2 instances, IPs, containers) that receive traffic based on the rules and listener configurations. Health checks are configured at the Target Group level.

### Critical CloudWatch Alarms

- `TargetResponseTime > 500ms` (p95 latency breach).
    
- `HTTPCode_Target_5XX_Count > 10` for 2 consecutive periods.
    
- `UnHealthyHostCount >= 1` per target group.
    
- `TargetConnectionErrorCount > 0`.

**With cross-zone load balancing enabled, one instance in Availability Zone X receives 20% traffic and four instances in Availability Zone Y receive 20% traffic each. With cross-zone load balancing disabled, one instance in Availability Zone X receives 50% traffic and four instances in Availability Zone Y receive 12.5% traffic each**

The nodes for your load balancer distribute requests from clients to registered targets. When cross-zone load balancing is enabled, each load balancer node distributes traffic across the registered targets in all enabled Availability Zones. Therefore, one instance in Availability Zone X receives 20% traffic and four instances in Availability Zone Y receive 20% traffic each. When cross-zone load balancing is disabled, each load balancer node distributes traffic only across the registered targets in its Availability Zone. Therefore, one instance in Availability Zone X receives 50% traffic and four instances in Availability Zone Y receive 12.5% traffic each.

Consider the following diagrams (the scenario illustrated in the diagrams involves 10 target instances split across 2 AZs) to understand the effect of cross-zone load balancing.

If cross-zone load balancing is enabled, each of the 10 targets receives 10% of the traffic. This is because each load balancer node can route its 50% of the client traffic to all 10 targets.

![](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/images/cross_zone_load_balancing_enabled.png)

 via - [https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html)

If cross-zone load balancing is disabled:

Each of the two targets in Availability Zone X receives 25% of the traffic.

Each of the eight targets in Availability Zone Y receives 6.25% of the traffic.

This is because each load balancer node can route its 50% of the client traffic only to targets in its Availability Zone

![](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/images/cross_zone_load_balancing_disabled.png)

 via - [https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html)
