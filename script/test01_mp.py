

import pytest
from api.api_mp import ApiMp
import api
from tool.read_yaml import read_yaml
from tool.tool import Tool
from tool.get_log import GetLog
log = GetLog.get_logger()
class TestMp:
    # 初始化
    def setup_class(self):
        # 获取api_mp对象 ,实例化需要小括号
        self.api_mp = ApiMp()
    # 登录接口测试方法
    @pytest.mark.parametriza('mobile,code',read_yaml("D:\python\pythonProject5\apitest\data\mp_login.yaml"))
    def test_mp_login(self,mobile,code):
        api_mp_login = self.api_mp.api_mp_login(mobile,code)
        print('打印的结果：',api_mp_login.json())
        try:
            # 提取token
            Tool.common_token(api_mp_login)
            # 断言状态码
            Tool.common_assert(api_mp_login)
        except Exception as e :
            # 写日志
            log.error(e)
            # 断言
            raise
            #
    # 发布文章测试接口方法
    @pytest.mark.parametriza('title,context,channel.id',read_yaml('D:\python\pythonProject5\apitest\data\mp_article.yaml'))
    def test_mp_article(self,title,context,channel_id):
        api_mp_article = self.api_mp.api_mp_article(title,context,channel_id)
        print('打印的结果：', api_mp_article.json())
        try:
            # 提取data_id
            api.article_id = api_mp_article.json().get('data').get("id")
            # 断言状态码
            assert Tool.common_assert(api_mp_article)

        except Exception as e :
            log.error(e)
            raise









