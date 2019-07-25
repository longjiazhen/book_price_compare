
def format_str():
    """ 格式化字符串 """
    name = '张三'
    print('欢迎您，%s' % name)
    # 整型，float类型
    num = 12.33
    print('您输入的数字是：%.4f' % num)
    num2 =54
    print('您的编号是：%04d' % num2)

    t = (1, 2, 3, 5)
    print('您输入的元组是：%s' % str(t))

    #print('您的姓名：%(name)s' % {'name': name})
    print('您的姓名：%s' % name)

def format_str_2():
    """ 用format格式化字符串 """
    # 使用位置
    print('欢迎您, {1}, {2} ---- {1}说'.format('张三','李四','好久不见'))

    # 使用名称
    d = {
        'userName': '赵六',
        'userNum': '66'
    }
    #print('您好, {userName}, 您的编号是 {userNum} '.format(userName = "王五", userNum = 45))
    print('您好, {userName}, 您的编号是 {userNum}'.format(**d))

    # 格式化元组
    point = (1, 6)
    print('坐标位置：{0[0]}:{0[1]}'.format(point))

    # 格式化类
    user = User('小可爱', 23)
    #print(user.show())
    print(user)

class User(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age
    def show(self):
        return '用户名：{self.username}，年龄：{self.age}'.format(self=self)
    def __str__(self):
        return self.show()


if __name__ == '__main__':
    format_str_2()