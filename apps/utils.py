from jsonschema import validate, ValidationError
from .errors import validated_error


def validate_argments(schema, argments):
    try:
        validate(schema, argments)
        return None
    except ValidationError as e:
        path = e.path

        if not path:
            message = e.message
            key = message[:message.rfind("'")].split("'")[-1]
        else:
            key = path[0]

        return validated_error(422, key)


def verify_argments(required, argments):
    if isinstance(argments, (dict,)):
        argments = [argments]

    for filed in required:
        for args in argments:
            if filed not in args:
                return validated_error(422, filed)
    return None


def convert_schema(schema):
    required = schema.pop('required', None)
    is_arrays = schema.pop('is_arrays', None)

    strand_schema = {
        'type': 'object',
        'properties': schema
    }
    if is_arrays:
        strand_schema = {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': schema
            },
        }

    if required:
        strand_schema.update(required=required)

    return strand_schema
