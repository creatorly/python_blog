import asyncio
import orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(user='root', password='root', db='awesome', loop=loop)
    #u = User(name='Test10', email='test8@example.com', passwd='123456', image='about:blank')
    u = Blog(id='2',user_id='123', user_name='lin',user_image='test.test', name='Test10',summary='ewe', content='kjasdhfkjhasdkfh')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()