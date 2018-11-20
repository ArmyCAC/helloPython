import socket
import datetime

start = datetime.datetime.now()

def nonblocking_way():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('www.baidu.com', 80))
    except OSError:
        pass

    request = 'GET / HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'
    data = request.encode('ASCII')

    # Don't know when the socked is ready, so keep trying send
    while True:
        try:
            sock.send(data)
            # send util has no exception throw, data is sended now
            break
        except OSError:
            pass

    response = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while True:
                response += chunk
                chunk = sock.recv(4096)
        except OSError:
            pass
    return response

def sync_way():
    res = []
    for i in range(10):
        res.append(nonblocking_way())
    return len(res)

if __name__ == '__main__':
    sync_way()
    end = datetime.datetime.now()
    print(end-start)