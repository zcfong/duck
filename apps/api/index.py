from . import api
from ..decorators import required_validate


@api.route('/index', methods=['POST'])
@required_validate({
    "name": {'type': 'string'},
    "required": ["name"],
    "is_arrays": False}
)
def fuck():
    return 'fuck'
