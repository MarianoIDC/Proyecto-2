import pika, sys, os, time, json

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    message = body.decode()
    with open('data.json', 'w') as f:
        json.dump(message, f)
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