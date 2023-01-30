## Virtualization and Cloud Basic


Review Getting Started with Amazon EC2. Log Into Your AWS Account, Launch, Configure, Connect and Terminate Your Instance. Do not use Amazon Lightsail. It is recommended to use the t2 or t3.micro instance and the CentOS operating system.

<em>Create and run instance.</em>

<img src="./docs/images/create_and_run_instance.png" />

<em>Connetct to instance.</em>

<em>Reset pem key in Windows OS</em>
<em>Set permissions</em>

icacls .\frankfurt.pem /reset
icacls .\frankfurt.pem /inheritance:r
icacls .\frankfurt.pem /grant:r "$($env:USERNAME):(R)"

<img src="./docs/images/connect_to_instance.png" />

<em>Delete instanse.</em>

<img src="./docs/images/terminate_instatnce.png" />

<img src="./docs/images/terminated_instatnce.png" />

<em>Create a snapshot of instance.</em>

<img src="./docs/images/create_snapshot.png" />

<em>Create and attach a Disk_D (EBS) to nstance.</em>

<img src="./docs/images/attach_volume.png" />

<img src="./docs/images/mount_volume.png" />

<em>Create and save some file on Disk_D</em>

<img src="./docs/images/create_file.png" />

<em>Deattach volume</em>

<img src="./docs/images/deattach_volume.png" />

<img src="./docs/images/success_deattach_volume.png" />

<em>Launch the second instance from backup.</em>

<img src="./docs/images/create_image.png" />

<img src="./docs/images/instance_from_image.png" />

<em>Attach disk_D to the new instance</em>

<img src="./docs/images/attach_volume_to_new_instance.png" />

<em>Free register the domain name*.PP.UA</em>

<img src="./docs/images/free_domain_name.png" />

<em>Create domain  name. Ping instance</em>

<img src="./docs/images/instance.png" />

<img src="./docs/images/ping_own_domain_name.png" />

<em>Launch and configure a WordPress instance with Amazon Lightsail</em>

<img src="./docs/images/lightsail_wordpress.png" />

<img src="./docs/images/console_wordpress.png" />

<img src="./docs/images/wp-admin.png" />

<em>Create bucket, upload files</em>

<img src="./docs/images/create_bucket.png" />

<em>Create user</em>

<img src="./docs/images/create_user_IAM.png" />

<em>Create access key</em>

<img src="./docs/images/create_access_key.png" />

<em>Configure CLI AWS and upload any files to S3.</em>

<img src="./docs/images/upload_to_bucket_from_CLI.png" />

<em>Deploy Docker Containers on Amazon Elastic Container Service (Amazon  ECS)</em>

<em>Create docker image</em>

<img src="./docs/images/create_docker.png" />

<em>Test</em>

<img src="./docs/images/hello_world_docker.png" />

<em>AWS Lambda</em>

<img src="./docs/images/lambda_hello_world.png" />

<em>Create a static website on Amazon S3</em>

<em>[EPAM Cloud&DevOps Fundamentals Autumn 2022](http://srg6rt-botnikov-1.s3-website.eu-central-1.amazonaws.com/)</em>