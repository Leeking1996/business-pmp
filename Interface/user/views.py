from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.content_db import get_db_content
from domain.users.schemy import *
from Interface.user import crud as user_crud
from utils import return_response

router = APIRouter()


@router.post("/user/login", summary="登录接口")
async def user_login(loginUser: LoginUser, db: Session = Depends(get_db_content)):
    return_data = await user_crud.login_user(loginUser.dict(), db)
    return return_response.message(return_data)
