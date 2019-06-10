import yaml
import socket
import json
from argparse import ArgumentParser

from actions import resolve
from protocol import (
    validation_request, make_response
)

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

            b_request = client.recv(buffersize)
            request = json.load(b_request.decode(encoding))

            if validation_request(request):
                action_name = request.get('action')
                controller = resolve(action_name)
                if controller:
                    try:
                        response = controller(request)
                    except Exception as err:
                        print(err)
                        response = make_response(request, 500, 'Internal server error')
                else:
                    response = make_response(request, 404, 'Action not found')
            else:
                response = make_response(request, 400, 'Wrong request')

            s_response = json.dumps(response)
            client.send(s_response.encode(encoding))
            client.close()

except KeyboardInterrupt:
    pass