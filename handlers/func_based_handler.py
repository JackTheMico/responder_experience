# -*- coding:utf-8 -*-
"""
-------------------------------------------------

    File Name:        /Users/jackdeng/code/Python/responder_exercise/handlers/func_based_handler.py

    Description:      func based handler demo

    Author:           liangwen.deng@kankanai.com.cn

    Date:             2019-04-11-11:20:15

    Version:          v1.0

    Lastmodified:     2019-04-11 by Jack Deng

-------------------------------------------------
"""
import random
import string

from datetime import date
from responder_api import api
from models.pet import PetSchema
# from marshmallow import Schema, fields

# @api.schema("Feeder")
# class FeederSchema(Schema):
#     name = fields.Str()
#     age = fields.Int()
#     gender = fields.Str()
#     hiredate = fields.Date()

# @api.schema("Pet")
# class PetSchema(Schema):
#     name = fields.Str()
#     age = fields.Int()
#     feeder = fields.Nested(FeederSchema())
#     category = fields.Str()

def random_str(size=6, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

@api.route("/pet")
def randowm_pet(req, resp):
    """A random furry pet endpoine.
    ---
    get:
        description: Get a random pet with feeders information
        responses:
            200:
                description: A pet to be returned
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/Pet'
    """
    feeder = {
        "name": random_str(size=random.randint(3,9)),
        "age": random.randint(19, 60),
        "gender": random.choice(["male", "female"]),
        "hiredate": date(2000, 11, 16)
    }
    pet = {
        "name": random_str(size=random.randint(3,9)),
        "age": random.randint(19, 60),
        "feeder": feeder,
        "category": random.choice(["cat", "dog", "parrot", "mouse", "panda"])
    }
    pet_schema = PetSchema()
    resp.media = pet_schema.dump(pet)
