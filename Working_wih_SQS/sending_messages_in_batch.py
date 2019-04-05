import boto3
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='example')

response = queue.send_messages(Entries=[
	{
		'Id': '1',
		'MessageBody': 'This fist message in example queue'
	},
	{
		'Id': '2',
		'MessageBody': 'This message also has some attributes',
		'MessageAttributes': {
			'Author': {
				'StringValue': 'Mayank Sachan',
				'DataType': 'String'
			}
		}
	}
])

print(response.get('Failed'))
