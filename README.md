# [Solution] DevOps Challenge
======================================

> Note:- To achieve this use-case we are using localstack to mock AWS API for S3. We will  run localstack server on top of single node kubernetes cluster which will run on top of virtualbox as a virtual machine.

#### Requirements:-
- Homebrew
- Docker
- VirtualBox
- Minikube
- Kubectl
- Helm
- awscli
- Python
- Localstack

## Setup Instructions

> Note: This setup is done on mac OS. If you are using different machine the installation instructions will differ.

#### Installing Homebrew

Follow the instruction mentioned in this url. 
https://brew.sh/

#### Installing Docker

Download 'docker.dmg' from link https://docs.docker.com/docker-for-mac/install/ and follow the setup wizard for installation.

#### Installing VirtualBox

Download 'virtualbox.dmg' from link https://www.virtualbox.org/wiki/Downloads and follow the setup wizard for installation.

#### Installing Minikube

Follow the instructions mentioned in this link. 
https://minikube.sigs.k8s.io/docs/start/

#### Installing Kubectl

Follow the instructions mentioned in this link.
https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/

#### Installing Helm

Follow the instructions mentioned in this link.
https://helm.sh/docs/intro/install/

#### Installing awscli

Follow the instructions mentioned in this link.
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html

#### Installing Python

Follow the instructions mentioned in this link.
https://www.python.org/downloads/

#### Installing Localstack

You can use Helm to install LocalStack in a Kubernetes cluster by running these commands (the Helm charts are maintained in this [repo](https://github.com/localstack/helm-charts)):
```sh
$ helm repo add localstack-repo http://helm.localstack.cloud
$ helm upgrade --install localstack localstack-repo/localstack
```
 
Once it's installed you will see a pod created which will be running localstack server also a NodePort service will be created for the deployment, which will give access to our localstack server api's.

```sh
$ kubectl get po
NAME                          READY   STATUS    RESTARTS   AGE
localstack-5755f6f77f-rh5hq   1/1     Running   1          18d

$ kubectl get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                         AGE
kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP                         18d
localstack   NodePort    10.106.49.66   <none>        4566:31566/TCP,4571:31571/TCP   18d

$ minikube ip
192.168.99.103
```

> Note:- LocalStack spins up core Cloud APIs on your local machine which can be checked via `http://<minikube-ip>:<NodePort>` in our case it would be http://192.168.99.103:31566/health

#### Configuring AWS profile

> Note:- Use **test** as AWS Access Key ID and AWS Secret Access Key for communicating to localstack server.
```sh
$ aws configure --profile localstack
```

#### Generating some data

Let's add some random generated files in our S3 bucket for testing. For that I have created a shell script as follows:-

> Note:- This script will gererate multiple files passed a list with some random data taken from the system. Later copy the files to S3 hosted on localstack server


**script.sh**

```sh
#!/bin/bash

# set -x
for filename in 'test' 'data' 'log' 'config' 'sys' 'network' 'logify' 'testify' 'system' 'configuration' 'testify'
do
	for number in {1..6}
	do
		aws --endpoint-url=http://192.168.99.103:31566/ --profile localstack s3 mb s3://bucket${number} 2> /dev/null
		head -c "${number}0" < /var/log/system.log > ${filename}file${number}.txt
		aws --endpoint-url=http://192.168.99.103:31566/ --profile localstack s3 mv ./${filename}file${number}.txt s3://bucket${number}
	done
done
```

#### Running the shell script

Give executable permissions to your shell script, as mentioned below before running.

```sh
$ chmod +x script.sh
$ ./script.sh
```

#### Writing the python script 

**substring_check.py**

```py
"""
This python program takes two arguments:- 1.s3 Bucket Name & 2.Sub-String (Pattern to search inside a file).
This program is used to search all files inside the given s3 bucket which contains the said Sub-String.
"""

import boto3

bucket_name, substring = input("Enter bucket_name:"), input("Enter string to search:")

# Creating boto3 session which typically stores AWS credentials.
custom_session = boto3.session.Session(profile_name="localstack")

# Resources represent high level interface to Amazon Web Services (AWS)
s3_resource = custom_session.resource(service_name="s3", endpoint_url="http://192.168.99.103:31566/")

try:
    # Setting a custom counter to handle a use-case where substring is not found in any of the files.
    found = 0   

    # This is an iterator which iterates to all object inside the given bucket
    for obj in s3_resource.Bucket(bucket_name).objects.all():
        
        # Reading the content of the object.
        body = obj.get()['Body'].read().decode('utf-8')
        
        # Condition to check if substring exists in object.
        if substring.lower() in body.lower():
            print(obj.key)
            found = 1

    if found == 0:
        print("Substring not found!")

except:
    print("Bucket doesn't exist.")
```

#### Running the python script

> Note:- While running the script you have to enter the s3 bucket name and the substring to search within the files inside S3 bucket.

```sh
$ python substring_check.py
```

This script will display all the files which includes the content wich maches the passed substring.

### Try it out!
