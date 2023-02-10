from fastapi import FastAPI
import uvicorn
from router.router import register_app
from utils.auto_create_models import auto_create_models
from utils.middleware import register_middleware


def init_app():
    project_app = FastAPI()

    """注册路由"""
    register_app(project_app)

    """中间件"""
    register_middleware(project_app)

    """自动创建表"""
    auto_create_models()

    return project_app


app = init_app()


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8030, reload=True)
