AWS Certificate Manager is a service that lets you <mark style="background:#fff88f">easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) </mark>certificates for use with AWS services and your internal connected resources. SSL/TLS certificates are used to secure network communications and establish the identity of websites over the Internet as well as resources on private networks. AWS Certificate Manager removes the time-consuming manual process of purchasing, uploading, and renewing SSL/TLS certificates.

A fully qualified domain name (FQDN) is the complete DNS name for a computer, website, or other resource connected to a network or to the internet. For example, aws.amazon.com is the FQDN for Amazon Web Services. An FQDN includes all domains up to the top–level domain. For example, [subdomain1].[subdomain2]...[subdomainn].[apex domain].[top–level domain] represents the general format of an FQDN.

To use a certificate with an Application Load Balancer for the same site (the same fully qualified domain name, or FQDN, or set of FQDNs) in a different Region, you must request a new certificate for each Region in which you plan to use it. To use an ACM certificate with Amazon CloudFront, you must request the certificate in the US East (N. Virginia) Region.

Therefore, to migrate the web applications to a multi-Region architecture, you must request a separate certificate for each FQDN in each AWS Region using AWS Certificate Manager and then associate the certificates with the corresponding ALBs in the relevant AWS Region.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt1-q40-i1.jpg)

 via - [https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html](https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html)

Incorrect options:

**Generate a certificate for each FQDN via AWS Certificate Manager. Associate the same FQDN certificate with the ALBs in the relevant AWS Regions** - As explained above, you cannot use the same certificate for a given FQDN across multiple AWS Regions, so this option is incorrect.

**Generate a new certificate for each FQDN in the relevant AWS Region using AWS KMS. Associate the certificate with the corresponding ALBs in the relevant AWS Region**

**Generate a separate certificate for each FQDN in each AWS Region using AWS KMS. Associate the certificates with the corresponding ALBs in the relevant AWS Region**

AWS KMS is a managed service that enables you to easily create and control the keys used for cryptographic operations. You can use KMS to centrally manage the encryption keys that control access to your data so that you can secure your data across AWS services. You cannot use KMS to provision or manage SSL/TLS certificates for an FQDN, so both these options are incorrect.

Reference:

[https://docs.aws.amazon.com/acm/latest/userguide/acm-Regions.html](https://docs.aws.amazon.com/acm/latest/userguide/acm-Regions.html)