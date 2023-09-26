import requests
import time
import api


class ApiApp:
    # 初始化
    def __init__(self):
        self.app_login_url = api.host+'app/v1_0/authorizations'
        self.app_article_url = api.host+'app/v1_1/articles'
    # 登陆接口的测试
    def app_login(self,mobile,code):
        data = {'mobile':mobile,'code':code}
        return requests.post(url=self.app_login_url,json =data ,headers=api.headers)
    # 获取频道下面的新闻
    def app_get_text(self):
        data={'channel_id':api.article_channel_id,"timestamp":int(time.time()),'with_top':1}
        return requests.get(url=self.app_article_url,params = data,headers=api.headers)
