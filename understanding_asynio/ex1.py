import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)

start = now()

# 生成一个协程对象，do_some_work 并没有执行
coroutine = do_some_work(2)
print(coroutine)

# 创建一个事件循环
loop = asyncio.get_event_loop()

# 将协程对象包装成为一个任务，再丢到事件循环中
# task 任务是 future 的子类
task = loop.create_task(coroutine)
print(task)


# 将协程对象丢到事件循环中
# loop.run_until_complete(coroutine)

# 将协程对象丢到事件循环中
loop.run_until_complete(task)
print(task)

print('Times: ',now()-start)




