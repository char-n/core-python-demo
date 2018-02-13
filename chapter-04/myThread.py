# encoding=utf-8

import threading


# 问题2 ,这个类怎么理解
class MyThread(threading.Thread):
    # name是默认参数
    def __init__(self, func, args, name=''):
        # 这一行代码是什么意思?
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        # print('start', self.name, 'at ', ctime())
        # 这里的*self.args 是可变参数
        self.res = self.func(*self.args)
        # print(self.name, 'finished at :', ctime())
