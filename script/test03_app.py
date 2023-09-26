from api.api_app import ApiApp
from tool.read_yaml import read_yaml
from tool.tool import Tool
from tool.get_log import GetLog
import pytest
log = GetLog.get_logger()

class TestApp:
    # 初始化
    def setup_class(self):
        self.api_app = ApiApp()


    # 登陆
    @pytest.mark.parametrize('channel_id,timestamp,with_top',read_yaml('D:\python\pythonProject5\apitest\data\app_login.yaml'))
    def test_app_login(self,mobile,code):
        res = self.api_app.app_login(mobile,code)
        # 将token放入头文件
        Tool.common_token(res)
        # 断言
        try:
            Tool.common_assert(res)
        except Exception as e:
            log.error(e)
            raise
    # 获取频道下的新闻
    def test_app_get_news(self):
        res = self.api_app.app_get_text()
        # 获取token
        # 将token放入头文件
        Tool.common_token(res)
        # 断言
        try:
            Tool.common_assert(res)
        except Exception as e:
            log.error(e)
            raise
