from flask import jsonify


def bad_request():
    return jsonify({'status': 400, 'msg': '验证错误'})


def validated_error(status, key):
    return jsonify({'status': status,
                    'msg': f'{key} 验证错误!', 'result': key})


def unauthorized():
    return jsonify({'status': '401', 'msg': '未授权'})


def forbidden():
    return jsonify({'status': '403', 'msg': '未登录'})
