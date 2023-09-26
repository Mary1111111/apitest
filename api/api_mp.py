import api
import requests

class ApiMp:
    # 初始化
    def __init__(self):
        # 定义登陆接口的URL
        self.url_login = api.host+'/mp/v1_0/authorizations'
        # 定义发布文章的url
        self.url_article = api.host+'mp/v1_0/articles'


    # 登陆接口
    def  api_mp_login(self,mobile,code):
        """

        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        # 定义请求的数据
        data = {'mobile':mobile,'code':code}
       # 调用post方法
        return requests.post(url = self.url_login,json = data,headers = api.headers)

    # 发布文章接口
    def api_mp_article(self,title,context,channel_id,):
        """

        :param title: 文章的标题
        :param context: 文章的内容
        :param channel_id: 文章的频道
        :return: 响应对象
        """
        # 定义请求数据
        data =  {'title':title,'context':context,"channel_id":channel_id,"cover":{"type":0,"images":[]}}
        # 调用post方法
        return  requests.post(url = self.url_article,json =data , headers=api.headers)
