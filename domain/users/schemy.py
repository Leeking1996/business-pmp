from pydantic import BaseModel, Field
from typing import Optional


class LoginUser(BaseModel):
    user_name: str = Field(title="用户名称")
    password: str = Field(title="用户密码")
    platform_code: str = Field(title="平台码")

