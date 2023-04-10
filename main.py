from fastapi import FastAPI
import uvicorn
from router.router import register_app
from utils.auto_create_models import auto_create_models
from utils.middleware import register_middleware

"""服务端口和服务名称"""
port = 8032
server_name = "pmp-config"


def init_app():
    project_app = FastAPI()

    """注册路由"""
    register_app(project_app)

    """中间件"""
    register_middleware(project_app)

    """自动创建表"""
    auto_create_models()

    """注册服务中心"""
    # consul_ = InitializationServer(server_name, port)
    # consul_.register()

    return project_app


app = init_app()

if __name__ == '__main__':
    # 初始化数据库, 把数据写入到数据库中

    uvicorn.run(app="main:app", host="0.0.0.0", port=port, reload=True)
