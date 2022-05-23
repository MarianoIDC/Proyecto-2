import os, pika, sys

PORT = os.getenv('RABBIT_PORT')
USER = os.getenv('RABBIT_USER')
PASSWORD = os.getenv('RABBIT_PASSWORD')
HOST = os.getenv('RABBIT_HOST')

credentials = pika.PlainCredentials(USER, PASSWORD)
parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))

print(" [x] Sent %r" % message)
connection.close()