'''公共变量'''

# 请求的域名
from tool.read_yaml import read_yaml

host = "http://ttapi.research.itcast.cn"
# 请求的信息投
headers = {'Content-Type':'application/json'}

# 文章id
article_id = None
# 获取发布文章的读取数据
data_article = read_yaml("D:\python\pythonProject5\apitest\data\mp_article.yaml")
print(data_article)

# 文章的标题
article_title =data_article[0]

#文章的内容
article_context =data_article[1]

# 文章的所属频道
article_channel_id = data_article[2]

print(article_title,article_context,article_channel_id )