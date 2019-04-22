import json
import time
from responder_api import api
from loguru import logger

@api.route('/user/{greeting}')
@api.route('/user/{greeting}/{num}')
# regular expression shity route like: /user(?:/(?P<id>.*?)(?:/(?P<action>.*?))?)?$
class Greetting:
    """
    class Greetting for
    """

    def on_request(self, req, resp, *args, **kwargs):
        logger.debug(f"on_request get {kwargs}")

    def on_get(self, req, resp, *args, **kwargs):
        """
        不是async 方法的话，会使用starlette的run_in_threadpool方法，将逻辑放在线程里跑
        """
        try:
            @api.background.task
            def background(s=10):
                time.sleep(s)
                logger.debug('sleep 10s done')

            background() # 后台任务，不会阻塞主线程
            greeting = kwargs['greeting']
            num = kwargs['num']
            logger.debug(f"on_get get {greeting}")
            resp.text = f"{greeting}, {num} world!"
            resp.headers.update({'X-Life': '42'})
            logger.debug(f"req session {req.session}")
            resp.session['username'] = 'admin'
            logger.debug(f"resp session {resp.session}")
        except KeyError as keye:
            logger.exception(keye)
            resp.text = f"KeyError {keye.__str__()}"
            resp.status_code = 400

    async def on_post(self, req, resp, *, greeting):
        """
        async 方法则使用asyncio 协程
        """
        logger.debug(f"on_post get {greeting}")
        req_json = await req.media()
        logger.debug(f"req media {req_json}")
        resp.media = req_json
