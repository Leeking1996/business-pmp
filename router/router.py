from starlette import status

from Interface.config.views import router as config_router
from Interface.user.views import router as user_router


def register_app(app):
    responses = {status.HTTP_404_NOT_FOUND: {"description": "Not Found"}}
    app.include_router(config_router, responses=responses)
    app.include_router(user_router, responses=responses)
