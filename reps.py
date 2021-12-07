#python3
import socket
import multiprocessing.dummy as md
def communicate(conn):
    while True:
        content = conn.recv(1024)
        if content[:5] == b'close':
            conn.close()
            break
        conn.send(content)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
with md.Pool(10) as pool:
    while True:
        conn, addr = s.accept()
        pool.apply_async(communicate, (conn, ))
    pool.join()
