import boto3

ec2 = boto3.resource('ec2')

res = ec2.create_instances(ImageId='ami-0cd3dfa4e37921605',MinCount=1,MaxCount=1,InstanceType='t2.micro',KeyName='AKVBQ5')

print(res[0].id)
