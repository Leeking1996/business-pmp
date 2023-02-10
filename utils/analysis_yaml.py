# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/2 23:06
"""解析 yaml文件"""

import yaml


def read_yaml_config():
    with open("/Users/king/PycharmProjects/business-pmp/configYaml/dev_setting.yaml", encoding="utf-8") as file:
        yaml_config = yaml.safe_load(file)
        return yaml_config