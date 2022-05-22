#!/usr/bin/env python
import pika, sys, os

def main():
<<<<<<< Updated upstream:applications/consumer/receive.py
    PORT = os.getenv('RABBIT_PORT')
    USER = os.getenv('RABBIT_USER')
    PASSWORD = os.getenv('RABBIT_PASSWORD')
    HOST = os.getenv('RABBIT_HOST')

    credentials = pika.PlainCredentials(USER, PASSWORD)
    parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)
    connection = pika.BlockingConnection(parameters)
=======
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
>>>>>>> Stashed changes:receive.py
    channel = connection.channel()

    channel.queue_declare(queue='message')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='message', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
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