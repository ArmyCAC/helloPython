import socket
import datetime
from concurrent import futures
import multiprocessing

start = datetime.datetime.now()
def blocking_way():
    sock = socket.socket()

    # blocking
    sock.connect(('www.baidu.com', 80))
    request = 'GET / HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'
    sock.send(request.encode('ASCII'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    return response

def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way())
    return len(res)

def process_way():
    # multiprocessing.freeze_support()
    workers = 10
    with futures.ProcessPoolExecutor(workers) as executor:
        # futs = {executor.submit(blocking_way) for i in range(10)}
        futs = []
        for i in range(10):
            futs.append(executor.submit(blocking_way))
    return len([fut.result() for fut in futs])

def thread_way():
    workers = 10
    with futures.ThreadPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])

# sync_way()
if __name__ == '__main__':
    # multiprocessing.freeze_support()
    # process_way()
    # print(process_way())
    thread_way()
    end = datetime.datetime.now()
    print('sync way needs: ' + str(end-start))
