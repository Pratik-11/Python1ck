import boto3



# S3_res = boto3.resource('s3')
# print('My S3 Buckets') 
# for bucket in S3_res.buckets.all():
#         print(bucket.name)

sts_client = boto3.client('sts', region_name='us-east-1')


assumed_role = sts_client.assume_role(
    RoleArn = 'arn:aws:iam::692859945317:role/PythonTest',
    
    RoleSessionName = 'AssumedRoleSession'
)
print(assumed_role)
credentials = assumed_role['Credentials']

session = boto3.Session(
    aws_access_key_id = credentials['AccessKeyId'],
    aws_secret_access_key = credentials['SecretAccessKey'],
    aws_session_token = credentials['SessionToken'],
)
ec2_client = session.client('ec2', region_name='us-east-1')
res = ec2_client.describe_instances()
# print(res)