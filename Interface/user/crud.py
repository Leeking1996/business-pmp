from sqlalchemy.orm import Session
from starlette import status

from utils import encryption
from domain.config.models import SysUser
from utils.verification import generate_access_token


async def login_user(loginUser: dict, db: Session):
    """登录接口"""
    response_data = {"message": "成功"}
    password = loginUser.get("password")
    user_name = loginUser.get("user_name")
    platform_code = loginUser.get("platform_code")
    encryption_password = encryption.MyDESCrypt().encrypt(password)
    judge_existence = db.query(SysUser).filter(SysUser.password == encryption_password, SysUser.person_num == user_name,
                                               SysUser.platform_code == platform_code).count()
    if judge_existence == 1:
        """如果存在，则需要把当前数据返回到前段"""
        data = {"password": encryption_password, "user_name": user_name, "platform_code": platform_code}
        token = generate_access_token(data)
        # 应该转换uuid进行返回，数据存储到redis中
        response_data.update({"token": token, "code": status.HTTP_200_OK})
    else:
        response_data["message"] = "登录失败，账号或密码错误"
        response_data.update({"code": status.HTTP_401_UNAUTHORIZED})
    return response_data
