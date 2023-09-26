# 定义函数

from  config import BASE_PATH
import yaml
import os
def  read_yaml(yaml_path):
    """

    :param yaml_path: 表示yaml文件的地址
    :return:  返回值为
    """
    # 定义空列表 组装测试数据
    arrs=[]
    # 获取文件流
    with open(yaml_path,'r',encoding='utf-8') as f:
        # 遍历调用yaml.safe_load(f).values()
        for datas in yaml.safe_load(f).values():
            arrs.append(tuple(datas.values()))
    return  arrs
