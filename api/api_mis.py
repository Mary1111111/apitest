import requests
import api

class ApiMis:
    # 初始化
    def __init__(self):
        self.mis_login_url = api.host +"mis/v1_0/authorizations"
        self.mis_article_url = api.host+'mis/v1_0/articles'
    # 管理员登陆测试

    def mis_login(self,account,password):
        data = {'account':account,"password":password}
        return  requests.post(url=self.mis_login_url,json = data,headers=api.headers)


    # 查询文章测试
    def  mis_search_article(self,):
        data = {"title":api.article_title,"channel":api.article_channel_id}
        return requests.get(url=self.mis_article_url,params = data,headers=api.headers)


     # 审核文章测试
    def mis_check_article(self):
        data = {"article_ids":[api.article_id],"status":2}
        return requests.put(url=self.mis_article_url, json=data, headers=api.headers)
