import www.orm
import asyncio
from www.models import User, Blog, Comment

async def test(loop):
    await www.orm.create_pool(loop=loop, user='root', password='Rtj19g9j@', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234qwer', image='about:blank')

    await u.save()

# loop = asyncio.get_event_loop()
# for x in test():
#     pass
# 要运行协程，需要使用事件循环
if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test(loop))
        print('Test finished.')
        loop.close()