import hashlib
import time
import os
import socket


def sha256(input_str):
    sha_signature = hashlib.sha256(input_str.encode()).hexdigest()
    return sha_signature


port = 60005
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(1024)

err_log = open('err_log', 'a')
login_log = open('login_log', 'a')

while True:
    try:
        conn, addr = s.accept()
        login_log.write(f'\n{time.asctime(time.localtime(time.time()))}\n{conn}\n{addr}')
    except Exception as e:
        err_log.write(f'\n{time.asctime(time.localtime(time.time()))}\n{e}')
