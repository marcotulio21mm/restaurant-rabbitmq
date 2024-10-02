import pika, sys, os
from receive import receive_message

def main():
    receive_message('hamburguer')
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('No longer accepts orders')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

