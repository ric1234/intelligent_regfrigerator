import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.21.77.95'))
parameters = pika.URLParameters('amqp://user:pass@192.168.141.195:5672/%2F')
connection = pika.BlockingConnection()
#connection = pika.BlockingConnection()
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello babe!')
print(" [x] Sent 'hey babe!'")
connection.close()
