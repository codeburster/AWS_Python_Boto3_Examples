import sys
from botocore.exceptions import ClientError
import boto3

ec2 = boto3.client('ec2')

instance_id = sys.argv[1].split(',')

#instance_id = sys.argv[1]
#print(type(instance_id))
#print(instance_id)

action = sys.argv[2].lower()

if action == "start":
	try:
		res = ec2.start_instances(InstanceIds=instance_id,DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			print("Something went wrong.")
			raise

	try:
		res = ec2.start_instances(InstanceIds=instance_id)
		print('instance started successfully')
	except ClientError as e:
		print('Error', e)

elif action == 'stop':
	try:
		res = ec2.stop_instances(InstanceIds=instance_id,DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			print("Something went wrong.")
			raise

	try:
		res = ec2.stop_instances(InstanceIds=instance_id)
		print('instance stopped successfully')
	except ClientError as e:
		print('Error', e)
else:
	print("Valid operations are [start/stop]")
