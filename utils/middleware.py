"""中间件"""
from fastapi import Request
from starlette.middleware.cors import CORSMiddleware
from utils import return_response
from utils.api_path import register_api_path


def register_middleware(app):
    origins = [
        "http://localhost",
        "http://localhost:8030",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def middleware(request: Request, call_next):
        # 获取 header中的token
        # header = request.headers
        # authorization = header.get("authorization")
        """验证token字段"""
        # if not authorization:
        #     return return_response.error(message="未识别 鉴权字段：Authorization")
        # else:
        #     response = await call_next(request)
        #     return response
        response = await call_next(request)
        return response