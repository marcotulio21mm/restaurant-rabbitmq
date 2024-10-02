#producer
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue='hamburguer')
channel.queue_declare(queue='pizza')
channel.queue_declare(queue='sushi')
channel.queue_declare(queue='tacos')

types = ['hamburguer', 'pizza', 'sushi', 'tacos']

def action_send_messages():
    while True:
        message = input("what would you like to order? ")
        if message == 'done':
            break
        if message not in types:
            print(f"the order of type {message} does not exist")
            continue
        channel.basic_publish(exchange='',
                    routing_key = message,
                    body=f'{message}')
        
action_send_messages()
        
print("[x] finished! ")
conn.close()