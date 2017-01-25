from marshmallow import Schema, fields


class BookSchema(Schema):

    title           = fields.String()
    desc            = fields.String()
    price           = fields.Number()
    asin            = fields.String()
    origin_link     = fields.Url()
    create_datetime = fields.DateTime()