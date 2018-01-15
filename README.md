### python 3.6
### 运行需要

*. 根目录建立.env文件
[settings]
DEBUG=True
REDIS_URL=redis://127.0.0.1:6379/5
DATABASE_URL=sqlite:///test.db
SECRET_KEY=xxoo
将相应的配置都加入其中

*. 整合数据库
  1. export FLASK_APP=manage.py
  2. flask db init
  3. flask db migrate
*. 测试环境执行
  flask run

*. 单元测试使用 pytest
*. 运营后台考虑使用flask admin

### todo
*. 用户登录
*. 后台操作日志
*. 权限模块
*. 后台管理
