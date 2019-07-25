import requests
from lxml import html

def spider(sn, book_list=[]):
    """ 爬取京东的数据 """
    # 获取html数据
    # F12找到相应请求，然后到 https://curl.trillworks.com/ 将curl请求转换成python报文头
    headers = {
        'authority': 'search.jd.com',
        'upgrade-insecure-requests': '1',
        'dnt': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'referer': 'https://search.jd.com/Search?keyword=9787115428028&enc=utf-8&pvid=419ee3ba300346ccae8a47ef995feee1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': '__jdc=122270672; unpl=V2_ZzNtbRdUF0Z0CEcGex5UBmIKF15LV0cTdglEXX1LVFdvVhFVclRCFX0UR1JnGlkUZwQZWEZcQxRFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHMcXw1gCxNVSmdzEkU4dld4HVoGZzMTbUNnAUEpD09TfBBeSG8GEVVFX0IdfThHZHg%3d; __jda=122270672.942969099.1563929346.1563929347.1563957911.2; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d2eb010c16924842815720387c9c9d29|1563957911320; areaId=19; ipLoc-djd=19-1607-3155-0; __jdu=942969099; shshshfpa=2cc52c9a-a296-5277-a18f-ebad6bc8d081-1563957916; PCSYCityID=1607; shshshfpb=o5pc8K4VPWDFbRoESDEkV7A%3D%3D; xtest=6924.cf6b6759; shshshfp=588f454735ec753e162d7ebd35bf15a0; rkv=V0500; 3AB9D23F7A4B3C9B=2IGXGQTIZ7QSL4MWU5K3YKDLKHJBBJHHO6UWERBZVNCNFZXUO7WRUL6ZCXII7ZVEY5DL7VPURIUPA72T6DJPSGACC4; qrsc=3; wlfstk_smdl=c8z8nyq0yabf290uvka12jmcstzuy0jb; __jdb=122270672.18.942969099|2.1563957911; shshshsID=2df840f8b945b0e2f2898f88582b1d50_10_1563960847803',
    }

    params = (
        ('keyword', '9787115428028'),
        ('enc', 'utf-8'),
        ('pvid', '4c66e7e1e36a4834a979be45c233f202'),
    )

    rest = requests.get('https://search.jd.com/Search', headers=headers, params=params)
    rest.encoding = 'utf-8'
    html_data = rest.text
    #print(html_data)

    # 获取xpath对象
    selector = html.fromstring(html_data)

    # 获取书本列表
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    #print(len(ul_list))
    for li in ul_list:
        # 标题
        title = li.xpath('div/div[@class="p-name"]/a/em/text()')
        #print(title[0])
        # 链接
        link = li.xpath('div/div[@class="p-name"]/a/@href')
        #print('https:' + link[0])
        # 价格
        price = li.xpath('div/div[@class="p-price"]/strong/i/text()')
        #print(price[0])
        # 商家
        #store1 = li.xpath('div/div[@class="p-shopnum"]/a/@title')
        store1 = li.xpath('div//a[@class="curr-shop hd-shopname"]/@title')
        store2 = li.xpath('div/div[@class="p-icons"]/i[@class="goods-icons J-picon-tips J-picon-fix"]/text()')
        if len(store1) == 0:
            store = '第三方商家'
        elif len(store2) != 0:
            store = '京东' + store2[0]
        else:
            store = store1[0]
        #print(store)

        book_list.append({
            'title': title[0],
            'price': price[0],
            'link': 'https:' + link[0],
            'store': store
        })

        #print('-------------------')

if __name__ == '__main__':
    sn = '9787115428028'
    spider(sn)