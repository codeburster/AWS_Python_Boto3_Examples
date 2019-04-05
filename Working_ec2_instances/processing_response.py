import boto3
ec2 = boto3.client('ec2')

res = ec2.describe_instances()
print(res)

# Process this JSON response
# using pandas

import pandas as pd

def instances_status(response):
	av_zones, instance_ids, state_names = [], [], []
	for res in response['Reservations']:
		for instance in res['Instances']:
			av_zones.append(instance['Placement']['AvailabilityZone'])
			instance_ids.append(instance['InstanceId'])
			state_names.append(instance['State']['Name'])
	return pd.DataFrame({
		'InstanceId': instance_ids,
		'AvailablityZone': av_zones,
		'State': state_names
	})


data_ec2 = instances_status(res)
print(data_ec2)


## I want to filter specific instances

res_stop = ec2.describe_instances(Filters=[{'Name': 'instance-state-name','Values':['stopped']}])
data_ec2_stop = instances_status(res_stop)
print(data_ec2_stop)


## I want to start the stopped instances
InstanceIds=list(data_ec2.loc[data_ec2['State'] == 'stopped', 'InstanceId'])
print(InstanceIds)

res = ec2.start_instances(InstanceIds=InstanceIds)
