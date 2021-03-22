from marshmallow import Schema, fields
from marshmallow.validate import Length


class Validation_Post(Schema):
    """ /api/note - POST
        Parameters:
         - title (str)
         - note (str)
         - user_id (int)
         - time_created (time)
        """
    title = fields.Str(required=True, error_messages={
                       "required": "Please provide title. It is a required field."},
                       validate=Length(max=100, min=5))
    image_path = fields.Str(required=True, error_messages={
                       "required": "Please provide image_path. It is a required field."}, validate=Length(max=200))
    description = fields.Str(required=True,error_messages={
                       "required": "Please provide description. It is a required field."},validate=Length(max=255))
    discount_price = fields.Int(required=True, error_messages={
        "required": "Please provide discount_price. It is a required field."})
    price = fields.Int(required=True, error_messages={
        "required": "Please provide price. It is a required field."})
    on_discount = fields.Boolean(required=True, error_messages={
        "required": "Please provide on_discount. It is a required field."})
    id = fields.Int(required=False)
    
class Validation_Put(Schema):
    title = fields.Str(required=True, error_messages={
        "required": "Please provide title. It is a required field."},
                       validate=Length(max=300, min=5))
    image_path = fields.Str(required=True, error_messages={
        "required": "Please provide image_path. It is a required field."}, validate=Length(max=200))
    description = fields.Str(required=True, error_messages={
        "required": "Please provide description. It is a required field."},
    validate = Length(max=255))
    discount_price = fields.Int(required=True, error_messages={
        "required": "Please provide discount_price. It is a required field."})
    price = fields.Int(required=True, error_messages={
        "required": "Please provide price. It is a required field."})
    on_discount = fields.Boolean(required=True, error_messages={
        "required": "Please provide on_discount. It is a required field."})
    id = fields.Int(required=True)
    

