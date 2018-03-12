import orm
import asyncio, logging
from models import User, Blog, Comment


async def test(loop): 

	await orm.create_pool(loop=loop,host='10.201.78.25', user='root', password='Link$2013', db='awesome')

	u = User(name='Test1', email='test@example.com1', passwd='1234567890', image='about:blank')

	await u.save()
loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

