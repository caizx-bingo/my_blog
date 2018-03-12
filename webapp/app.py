import logging; logging.basicConfig(level=logging.INFO)

from aiohttp import web
from coroweb import get
import asyncio

from webapp.coroweb import init_jinja2, add_routes, add_static, logger_factory, response_factory, datetime_filter


@get('/')
async def index(request):
    return '<h1>Awesome</h1>'


@get('/hello')
async def hello(request):
    return '<h1>hello!</h1>'


if __name__ == '__main__':
    async def init(loop):
        app = web.Application(loop=loop, middlewares={logger_factory, response_factory})
        init_jinja2(app, filters=dict(datetime=datetime_filter))
        add_routes(app, 'test_view')
        add_static(app)
        srv = await loop.create_server(app.make_handler(), 'localhost', 9000)
        logging.info('server started at http://127.0.0.1:9000...')
        return srv


    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()