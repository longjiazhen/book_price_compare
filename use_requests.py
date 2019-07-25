import requests

def get_book(sn):
    """获取书本信息"""
    url = 'http://search.dangdang.com/'
    rest = requests.get(url, params={
        'key': sn,
        'act': 'input'
    })
    # 以文本方式获取数据
    print(rest.text)
    # 以json的方式获取数据
    #if rest.text != '':
    #    print(rest.json())
    #rest.raw()
    #rest.content()
    #print(rest.status_code) # http 请求码
    #print(rest.encoding)
    #rest.encoding = 'utf-8'
    #print(rest.encoding)

if __name__ == '__main__':
    get_book('9787115428028')