import boto3
sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='example')

# process messages 
for message in queue.receive_messages(MessageAttributeNames=['Author']):
	#if message.message_attributes is not None:
	#	author_name = message.message_attributes.get('Author').get('StringValue')
#		if author_name:
#			author_text = ' ({0})'.format(author_name)

#	print('Hello, {0}!{1}'.format(message.body,author_text))
	print(message.body)
	message.delete()
