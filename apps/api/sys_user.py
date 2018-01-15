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
    'requires': ['name', 'email', 'password'],
})
def add_user():
    payload_data = request.json
    email = payload_data['email']
    sys_user = SysUser.query.filter(SysUser.email == email).first()

    if sys_user:
        return jsonify({'status': '411', 'msg': '该邮箱已存在!'})
    user = SysUser(**payload_data)
    db.session.add(user)
    db.session.commit()
    return jsonify({'status': '200', 'msg': '操作成功！'})


@api.route('/users', methods=['GET'])
def get_user():
    users = SysUser.query.all()
    user_collection = []
    for user in users:
        user_collection.append(user.to_json())
    return jsonify({'status': '200', 'msg': '操作成功!',
                    'result': user_collection})
