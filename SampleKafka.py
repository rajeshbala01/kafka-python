
from kafka import KafkaProducer

print('Start Producer ')
producer = KafkaProducer(bootstrap_servers='ec2-18-234-161-165.compute-1.amazonaws.com:9092')
producer.send('TestTopic1', b'Hello, World!')
print('First message posted')
producer.send('TestTopic1', key=b'message-two', value=b'This is Kafka-Python')
producer.close()
print('End Producer')

