# -*- coding:utf-8 -*-
"""
-------------------------------------------------

    File Name:        /Users/jackdeng/code/Python/responder_exercise/app.py

    Description:      exercise for responder

    Author:           liangwen.deng@kankanai.com.cn

    Date:             2019-04-10-16:08:05

    Version:          v1.0

    Lastmodified:     2019-04-10 by Jack Deng

-------------------------------------------------
"""

from responder_api import api
from handlers.class_based_handler import Greetting
from handlers.graphql_handler import Query
from handlers.func_based_handler import random_str

@api.route("/")
async def hello_world(req, resp):
    resp.text = 'Hello World!'

if __name__ == '__main__':
    api.run(
        address='127.0.0.1',
        port=8888,
        debug=False,
        log_level='info', # default level info
        workers=1)
