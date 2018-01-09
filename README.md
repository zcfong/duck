### python 3.6
### 运行需要

1. 根目录建立.env文件
[settings]
DEBUG=True
REDIS_URL=redis://127.0.0.1:6379/5
DATABASE_URL=sqlite:///test.db
SECRET_KEY=xxoo
将相应的配置都加入其中
2. 测试环境中使用
python mange.py

3. 单元测试使用 pytest
4. 运营后台考虑使用flask admin

### todo
1. 用户登录
2. 后台操作日志
3. 权限模块
4. 后台管理
