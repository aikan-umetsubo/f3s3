import boto3

s3 = boto3.client('s3')
response = s3.get_object(
    Bucket='f3s3-test',
    Key='testFile'
)

print(response['Body'].read())
