**CloudFront by default, forwards the requests to the default S3 endpoint. Change the origin domain name of the distribution to include the Regional endpoint of the bucket**  -  [[Amazon S3]]

You can use the `Cache-Control` and `Expires` headers to control how long objects stay in the CloudFront cache. 