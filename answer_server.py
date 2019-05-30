import yaml
import socket
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file',
    required=True
)

args = parser.parse_args()

host = 'localhost'
port = 8000
buffersize = 1024
encoding = 'utf-8'

if args.config:
    with open(args.config) as file:
        config = yaml.load(file, Loader=yaml.Loader)
        host = config.get('host')
        port = config.get('port')


try:
        sock = socket.socket()

        sock.bind((host, port))
        sock.listen(5) #5 запросов обрабатывает
        print(f'Server was started with {host}:{port}')

        while True:
        #процесс обработки
            client, address = sock.accept()
            print(f'Client was detected{address}')
            data = client.recv(buffersize)
            print(data.decode(encoding))
            client.send(data)
            client.close() #завершаем работу

except KeyboardInterrupt:
    pass