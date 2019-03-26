from sanic import Sanic
from views import bp

app = Sanic(__name__)

db_settings = {
    'DB_HOST': 'localhost',
    'DB_NAME': 'appdb',
    'DB_USER': 'appuser'
}


# 注册配置
app.config.update(db_settings)
# 注册蓝图路由
app.blueprint(bp)



