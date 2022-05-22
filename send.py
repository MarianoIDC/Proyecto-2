import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='message')

channel.basic_publish(exchange='',
                      routing_key='message',
                      body='Hello World!, Mariano')
print(" [x] Sent 'Hello World!'")

connection.close()