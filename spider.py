from spider_dangdang import spider as dangdang
from spider_jb import spider as jd
from spider_yhd import spider as yhd


def main(sn):
    """ 图书比价工具 """
    book_list = []
    # 当当网的数据
    dangdang(sn, book_list)
    print('当当网的数据爬取完成')
    # 京东的数据
    print('京东的数据爬取完成')
    jd(sn, book_list)
    # 一号店的数据
    print('一号店的数据爬取完成')
    yhd(sn, book_list)
    # 打印所有数据列表
    #for book in book_list:
    #    print(book)
    print('************** 开始排序 ***************')
    # 排序书的数据
    book_list =  sorted(book_list, key=lambda item: float(item["price"]), reverse=False)
    for book in book_list:
        print(book)


if __name__ == '__main__':
    sn = input('请输入ISBN: ')
    # 9787115428028
    main(sn)