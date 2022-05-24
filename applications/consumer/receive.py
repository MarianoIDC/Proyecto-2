#!/usr/bin/env python
from email import message
import pika, sys, os, time

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    message = "Goodbye World!"
    ch.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
    ch.close()

def main():
    PORT = os.getenv('RABBIT_PORT')
    USER = os.getenv('RABBIT_USER')
    PASSWORD = os.getenv('RABBIT_PASSWORD')
    HOST = os.getenv('RABBIT_HOST')

    credentials = pika.PlainCredentials(USER, PASSWORD)
    parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)