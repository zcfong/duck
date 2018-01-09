from . import api
from .. import db
from flask import jsonify, request
from ..decorators import required_validate
from ..models import SysUser


@api.route('/user', methods=['POST'])
@required_validate({
    'name': {'type': 'string'},
    'email': {'type': 'string',
              'pattern': '^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'},
    'password': {'type': 'string'},
    'required': ['name', 'email', 'password']
})
def add_user():
    # payload_data = request.json
    # email = payload_data['email']
    # sys_user = SysUser.query.filter(SysUser.email == email).first()
    #
    # if sys_user:
    #     return jsonify({'status': '411', 'msg': '该邮箱已存在!'})
    # user = SysUser.from_json(request.json)
    # db.session.add(user)
    # db.session.commit()
    return jsonify({'status': '200', 'msg': '操作成功！'})
