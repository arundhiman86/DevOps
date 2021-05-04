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
