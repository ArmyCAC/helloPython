import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)

    # 模拟阻塞，该协程对象交出对 loop 的控制权，loop 调用其他协程对象
    await asyncio.sleep(x)
    return ('Done after {}s'.format(x))

start = now()

# 生成一个协程对象，do_some_work 并没有执行
coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

# 创建一个事件循环
loop = asyncio.get_event_loop()

# 将协程对象包装成为一个任务，再丢到事件循环中
# task 任务是 future 的子类
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]


# 将协程对象丢到事件循环中
# loop.run_until_complete(coroutine)

# 将协程对象丢到事件循环中
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print("Task ret:", task.result())

print('Times: ',now()-start)




