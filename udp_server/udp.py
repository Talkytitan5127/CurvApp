import socket
import requests
import json


HOST = '127.0.0.1'
PORT = 10001

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket:
    socket.bind((HOST, PORT))

    while True:
        data, addr = socket.recvfrom(1024)
        data = data.strip()
        if not data:
            break
        data = data.decode()
        print('Server accept: ', data)
        if data == 'echo':
            socket.sendto('server echo'.encode(), addr)
        url = 'http://127.0.0.1:5000/api/user/{}'.format(data)
        print(url)
        resp = requests.get(url)
        print(resp)
        print(resp.text)
        if resp.status_code != 200:
            break
        resp_data = json.loads(resp.text)
        print('Answer from tcp server: ', resp_data)
        fio = '{} {}'.format(resp_data['first_name'], resp_data['last_name'])
        socket.sendto(fio.encode(), addr)
        