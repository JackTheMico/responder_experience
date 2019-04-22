from responder_api import api
from marshmallow import Schema, fields

@api.schema("Feeder")
class FeederSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    gender = fields.Str()
    hiredate = fields.Date()

@api.schema("Pet")
class PetSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    feeder = fields.Nested(FeederSchema())
    category = fields.Str()
