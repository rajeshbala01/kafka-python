
from kafka import KafkaProducer


print('Start Producer ')
producer = KafkaProducer(bootstrap_servers='ec2-3-80-198-180.compute-1.amazonaws.com:9092')
g = input("Enter your real path of the file : ") 
f = open(g, "r")
content = f.read()
producer.send('test-topic', bytes(content, 'UTF-8'))
producer.close()
print('End Producer')

