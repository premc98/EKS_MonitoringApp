import boto3

ecr_client = boto3.client('ecr', region_name='us-east-1')

response = ecr_client.create_repository(repositoryName = "flask_monitoring_app_repo")

uri = response['repository']['repositoryUri']

print(uri)