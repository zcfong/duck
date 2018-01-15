from flask import request

from functools import wraps
from .utils import (convert_schema, validate_argments,
                    verify_argments)
from .errors import bad_request


def required_validate(schema):
    def decorator(f):
        @wraps(f)
        def validated_func(*args, **kwargs):
            payload_data = request.json
            if not payload_data:
                return bad_request()
            requires = schema.get('requires', None)

            verify = verify_argments(requires, payload_data)
            if verify:
                return verify

            validated_schema = convert_schema(schema)
            validated = validate_argments(validated_schema,
                                          payload_data)
            if validated:
                return validated

            return f(*args, **kwargs)

        return validated_func

    return decorator
