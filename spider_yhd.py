import requests
from lxml import html

def spider(sn, book_list=[]):
    """ 爬取一号店的数据 """
    url = 'https://search.yhd.com/c0-0/k{sn}/'.format(sn=sn)
    # 获取html内容
    html_data = requests.get(url).text
    #print(html_data)
    # 获取xpath对象
    selector = html.fromstring(html_data)
    # 找到书本列表
    ul_list = selector.xpath('//div[@id="itemSearchList"]/div')
    #print(len(ul_list))
    for li in ul_list:
        # 标题
        #title = li.xpath('div//a[@class="mainTitle"]/@title')
        title = li.xpath('div//p[@class="proName clearfix"]/a/@title')
        #print(title[0])
        # 购买链接
        link = li.xpath('div//p[@class="proName clearfix"]/a/@href')
        #print('https:' + link[0])
        # 价格
        price = li.xpath('div//p[@class="proPrice"]/em/text()')
        #print(price[1].replace('\n',''))
        # 商家
        store1 = li.xpath('div//p[@class="searh_shop_storeName storeName limit_width"]\
        /span[@class="subscribe_self"]/text()')
        store2 = li.xpath('div//p[@class="searh_shop_storeName storeName limit_width"]\
        /a/span[@class="shop_text"]/text()')
        if len(store1) != 0:
            store = '一号店' + store1[0]
        else:
            store = store2[0]
        #print(store)

        book_list.append({
            'title': title[0],
            'price': price[1].replace('\n',''),
            'link': 'https:' + link[0],
            'store': store
        })

        #print('-----------------------')

if __name__ == '__main__':
    sn = '9787115428028'
    spider(sn)