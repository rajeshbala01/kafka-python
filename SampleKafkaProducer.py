
from kafka import KafkaProducer
from readFile import read_file

print('Start Producer ')
producer = KafkaProducer(bootstrap_servers='ec2-18-234-161-165.compute-1.amazonaws.com:9092')
g = input("Enter your real path of the file : ") 
f = open(g, "r")
for x in f:
 producer.send('TestTopic1', bytes(x, 'UTF-8'))
producer.close()
print('End Producer')

