from starlette import status

from Interface.config.views import router as config_router
from Interface.user.views import router as user_router
from Interface.team.views import router as team_router
from Interface.project_plan.views import router as project_plan_router
from Interface.score.views import router as score_router


def register_app(app):
    responses = {status.HTTP_404_NOT_FOUND: {"description": "Not Found"}}
    app.include_router(config_router, responses=responses)
    app.include_router(user_router, responses=responses)
    app.include_router(team_router, responses=responses)
    app.include_router(project_plan_router, responses=responses)
    app.include_router(score_router, responses=responses)
