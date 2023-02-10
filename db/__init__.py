import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

env = os.getenv("ENV")
if env == "DEV":
    from settings.dev_setting import mysql_db_dict
elif env == "PRO":
    from settings.pro_settings import mysql_db_dict
else:
    from settings.dev_setting import mysql_db_dict

# 初始化时，生成数据库链接，外层直接调用，单体用户不用考虑其他，

content_mysql_url = F"mysql+pymysql://" \
                    F"{mysql_db_dict.get('USERNAME')}:" \
                    F"{mysql_db_dict.get('PASSWORD')}@" \
                    F"{mysql_db_dict.get('HOST')}:{mysql_db_dict.get('POST')}/" \
                    F"{mysql_db_dict.get('DATABASES')}?charset=utf8"

engine = create_engine(url=content_mysql_url, pool_size=200, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
