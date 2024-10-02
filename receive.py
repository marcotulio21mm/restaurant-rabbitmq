import pika, sys, os, time

def receive_message(queueName):
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = conn.channel()

    channel.queue_declare(queue=queueName)

    def callback(ch, method, properties, body):
        print(f"[x] Order of {body} received!")
        time.sleep(3)
        print('order finished!')
    
    channel.basic_consume(queue=queueName, auto_ack=True, on_message_callback=callback)

    print(' [*] Waiting for orders. To exit press CTRL+C')

    channel.start_consuming()
    
if __name__ == '__receive_message__':
    try:
        receive_message()
    except KeyboardInterrupt:
        print('No longer accepts orders')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

