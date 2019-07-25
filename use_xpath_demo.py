from lxml import html

def parse():
    """将html文件中的内容，用xpath进行提取"""
    # 读取文件中的内容
    f = open("./static/index.html", 'r', encoding='utf-8')
    s = f.read()
    selector = html.fromstring(s)

    # 解析H3标题
    h3 = selector.xpath('/html/body/h3/text()')
    # 使用/是从根路径开始匹配，使用//是从指定路径开始匹配
    print(h3[0])

    # 解析ul下面的内容
    # ul = selector.xpath('/html/body/ul/li')
    ul = selector.xpath('//ul/li')
    print(len(ul))
    for li in ul:
        print(li.xpath('text()')[0])

    # 解析ul2下指定的元素值
    ul2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')
    # 使用 [@class="important"] 获取属性的元素值
    print(ul2[0])

    # 解析a标签下的内容
    # 标签内的内容
    a = selector.xpath('//div[@id="container"]/a/text()')
    print(a[0])
    # href 属性
    alink = selector.xpath('//div[@id="container"]/a/@href')
    print(alink[0])

    # 解析p标签
    p = selector.xpath('/html/body/p[last()]/text()')
    print(p[0])


    # 从浏览器复制来的xpath
    p5 = selector.xpath('//*[@id="container"]/p[5]/text()')
    print(p5[0])

    f.close()

if __name__ == '__main__':
    parse()