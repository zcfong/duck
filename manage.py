from apps import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)


@app.cli.command()
def init_db():
    # 初始化数据库
    db.create_all()


@app.cli.command()
def test():
    # todo 执行所有单元测试，没问题再推送master
    pass


@app.cli.command()
def deploy():
    pass


if __name__ == '__main__':
    app.run()
