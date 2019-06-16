import yaml
import socket
import json
import logging

from handlers import handle_default_request
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

#logger = logging.getLogger('main')
#formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#file_handler = logging.FileHandler('main.log', encoding='UTF-8')

#file_handler.setFormatter(formatter)
#file_handler.setLevel(logging.debug)

#logger.addHandler(file_handler)
#logger.addHandler(logging.StreamHandler())
#logger.setLevel(logging.debug)

try:
    sock = socket.socket()

    sock.bind((host, port))
    sock.listen(5)
    logger.info(f'Server was started with {host}:{port}')

    while True:
    #процесс обработки
        client, address = sock.accept()

        b_request = client.recv(buffersize)
        b_response = handle_default_request(b_request)
        client.send(b_response)
        client.close()

except KeyboardInterrupt:
    pass