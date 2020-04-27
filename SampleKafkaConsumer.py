from kafka import KafkaConsumer, TopicPartition

print('Start Consumer')
consumer = KafkaConsumer(bootstrap_servers='ec2-18-234-161-165.compute-1.amazonaws.com:9092',
                                 group_id='Consumer-group1' ,
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
##consumer.subscribe(['TestTopic1'])
tp = TopicPartition('TestTopic1', 0)
consumer.assign([tp])
consumer.poll(1000)
for message in consumer:
  print (message.partition, message.offset, message.value)
consumer.close()
print('End Consumer')