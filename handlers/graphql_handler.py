# -*- coding:utf-8 -*-
"""
-------------------------------------------------

    File Name:        /Users/jackdeng/code/Python/responder_exercise/handlers/graphql_handler.py

    Description:      GraphQL demo

    Author:           dlwxxxdlw@gmail.com

    Date:             2019-04-11-10:20:01

    Version:          v1.0

    Lastmodified:     2019-04-11 by Jack Deng

-------------------------------------------------
"""

import graphene
from loguru import logger
from responder.ext import GraphQLView
from responder_api import api

class Query(graphene.ObjectType):

    hello = graphene.String(name=graphene.String(default_value="stranger"))
    interesting = graphene.String(name=graphene.String(default_value="really interesting"))

    def resolve_hello(self, info, name):
        return f"Hello {name}"

    def resolve_interesting(self, info, name):
        req = info.context['request']
        resp = info.context['response']
        logger.debug(f"req {req}")
        logger.debug(f"resp {resp} text {resp.text}")
        return f"I wonder how it route {name}"

schema = graphene.Schema(query=Query)
view = GraphQLView(api=api, schema=schema)

api.add_route('/graph', view)
logger.debug("api load graphql view route")
