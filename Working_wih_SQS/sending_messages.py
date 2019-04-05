import boto3

sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='example')

response = queue.send_message(MessageBody="Hello World")

print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))


## Custom Message Attributes
cus_response = queue.send_message(MessageBody='I like Boto3', MessageAttributes={
			'Author': {
				'StringValue': 'Mayank',
				'DataType': 'String'
			},
			'Author_Email': {
				'StringValue': 'mayank.sachan@koenig-solutions.com',
				'DataType': 'String'
			}
		}
	)

print(response)
