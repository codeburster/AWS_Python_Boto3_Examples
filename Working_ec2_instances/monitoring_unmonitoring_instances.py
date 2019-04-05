import sys
import boto3

ec2 = boto3.client('ec2')

if sys.argv[1] == 'ON':
	res = ec2.monitor_instances(InstanceIds=[sys.argv[2]])
elif sys.argv[1] == 'OFF':
	res = ec2.unmonitor_instances(InstanceIds=[sys.argv[2]])
else:
	print("Not a valid argument: Valid arguments are [ON/OFF]")

print(res)
