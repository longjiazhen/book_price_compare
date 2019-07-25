import requests
from lxml import html

def spider(sn):
    """ 爬取淘宝网的数据 """
    # 获取html数据
    url = 'https://s.taobao.com/search?q=9787115428028'
    html_data = requests.get(url).text
    print(html_data)
    # 获取xpath对象
    # 获取书本列表
    # 标题
    # 购买链接
    # 价格
    # 商家
    print('----------------')


if __name__ == '__main__':
    sn = '9787115428028'
    spider(sn)