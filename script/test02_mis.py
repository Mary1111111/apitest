from api.api_mis import ApiMis
from tool.read_yaml import read_yaml
from tool.tool import Tool
from tool.get_log import GetLog
log = GetLog.get_logger()
import pytest

class TestMis:
    # 初始化
    def set_up(self):
        # 实例化对象
        self.api_mis = ApiMis()

    # 登入测试
    @pytest.mark.parametriza('account,password', read_yaml("D:\python\pythonProject5\apitest\data\mis_article.yaml"))
    def test_mis_login(self,account,password):
        res = self.api_mis.mis_login(account,password)
        # 获取token
        token = res.json().get('data').get('token')
        # 将token填入信息头部
        Tool.common_token(token)
        # 断言
        try:
            assert Tool.common_assert(res,status_code=200)
        except Exception as e:
            log.error(e)
            raise


    # 文章查找测试
    def test_mis_search_article(self):
        res = self.api_mis.mis_search_article()
        try:
            assert Tool.common_assert(res)
        except Exception as e:
            log.error(e)
            raise


    # 文章审核测试
    def  test_mis_check_article(self):
        res = self.api_mis.mis_check_article()
        try:
            assert Tool.common_assert(res.json())
        except Exception as e:
            log.error(e)
            raise

