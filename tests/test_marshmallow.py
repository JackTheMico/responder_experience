# -*- coding:utf-8 -*-
"""
-------------------------------------------------

    File Name:        /Users/jackdeng/code/Python/responder_exercise/tests/test_marshmallow.py

    Description:      test for openapi / marshmallow

    Author:           liangwen.deng@kankanai.com.cn

    Date:             2019-04-11-13:45:35

    Version:          v1.0

    Lastmodified:     2019-04-11 by Jack Deng

-------------------------------------------------
"""

import pytest
import random
import string
from ..responder_api import api as myapi
from datetime import date
from loguru import logger
from marshmallow import Schema, fields

@pytest.fixture
def api():
    return myapi

@myapi.schema("Feeder")
class FeederSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    gender = fields.Str()
    hiredate = fields.Date()

@myapi.schema("Pet")
class PetSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    feeder = fields.Nested(FeederSchema())
    category = fields.Str()

def random_str(size=6, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

@myapi.route("/pet")
async def randowm_pet(req, resp):
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


def test_response(api):
    r = api.session().get("http://;/schema.yml")
    assert "Pet" in r.text
