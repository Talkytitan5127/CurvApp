import socket
import requests
import json
import os
from signal import SIGINT, signal

HOST = os.getenv('UDP_HOST', default='127.0.0.1')
PORT = os.getenv('UDP_PORT', default=10001)


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket:
    socket.bind((HOST, PORT))

    while True:
        signal(SIGINT, lambda x, y: exit(0))

        data, addr = socket.recvfrom(1024)
        data = data.strip()
        if not data:
            continue

        # 17:16:27;07-03-20;1
        data = data.decode()
        print('Server accept: ', data)
        time_str, date_str, user_id = data.split(';')
        
        if data == 'echo':
            socket.sendto('server echo'.encode(), addr)
        url = 'http://127.0.0.1:5000/api/user/{}'.format(user_id)
        print(url)
        resp = requests.get(url, params={'time': time_str, 'date': date_str})
        print(resp)
        print(resp.text)
        if resp.status_code == 200:
            resp_data = json.loads(resp.text)
            timedate = resp_data['time']
            print('Answer from tcp server: ', resp_data)
            fio = '{};{} {}'.format(timedate, ['first_name'], resp_data['last_name'])
            socket.sendto(fio.encode(), addr)
        elif resp.status_code == 404:
            socket.sendto('not_found'.encode(), addr)
        else:
            socket.sendto('server error'.encode(), addr)