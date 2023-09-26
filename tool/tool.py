
import api
class Tool:
    # 提取token
    @classmethod
    def  common_token(cls,response):
        # 提取token
        token = response.json('data').get('token')
        # 追加请求信息头
        api.headers['Authorzation'] = 'Bearer' +token
        print('添加token后的headers为：',api.headers)


    # 断言
    @classmethod
    def common_assert(cls,response,status_code=201,):
        # 断言状态码
        assert status_code == response.status_cpde
        # 断言响应信息
        assert "ok" ==response.json().get('message')

