A company has its flagship application fronted by an Application Load Balancer that is targeting several EC2 Linux instances running in an Auto Scaling group in a private subnet. AWS Systems Manager Agent is installed on all the EC2 instances. The company recently released a new version of the application, however, some of the EC2 instances are now being marked as unhealthy and are being terminated, thereby causing the application to run at reduced capacity. You have been tasked to ascertain the root cause by analyzing Amazon CloudWatch logs that are collected from the application, but you find that the logs are inconclusive.

Which of the following options would you propose to get access to an EC2 instance to troubleshoot the issue?

**Suspend the Auto Scaling group's `Terminate` process. Use Session Manager to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause**

The `Terminate` process removes instances from the Auto Scaling group when the group scales in, or when Amazon EC2 Auto Scaling chooses to terminate instances for other reasons, such as when an instance is terminated for exceeding its maximum lifetime duration or failing a health check. You need to suspend the `Terminate` process which will allow you to get access to the instance without it being terminated even if it is marked as unhealthy. You should note that another way to prevent Amazon EC2 Auto Scaling from terminating unhealthy instances, is to suspend the `ReplaceUnhealthy` process. You can then leverage the Session Manager to log in to the instance that is marked as unhealthy and analyze the system logs to figure out the root cause.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q17-i1.jpg)

 via - [https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q17-i2.jpg)

 via - [https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

Incorrect options:

**Suspend the Auto Scaling group's `HealthCheck` process. Use EC2 instance connect to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause** - The `HealthCheck` process checks the health of the instances and marks an instance as unhealthy if Amazon EC2 or Elastic Load Balancing tells Amazon EC2 Auto Scaling that the instance is unhealthy. This process can override the health status of an instance that you set manually. If you suspend the `HealthCheck` process, then none of the instances would be marked as unhealthy. Therefore, you cannot suspend the `HealthCheck` process for the given use case, since you must identify the root cause behind some of the instances being marked as unhealthy.

**Suspend the Auto Scaling group's `Launch` process. Use Session Manager to log in to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause** - The `Launch` process adds instances to the Auto Scaling group when the group scales out, or when Amazon EC2 Auto Scaling chooses to launch instances for other reasons, such as when it adds instances to a warm pool. Suspending the `Launch` process will not help in identifying the root cause behind some instances being marked as unhealthy as those instances would still be terminated.

**Enable EC2 instance termination protection. Use Session Manager to log In to an instance that is marked as unhealthy and analyze the system logs to figure out the root cause** - Enabling EC2 instance termination (DisableApiTermination attribute) does not prevent Amazon EC2 Auto Scaling from terminating an instance.

References:

[https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination)

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html)