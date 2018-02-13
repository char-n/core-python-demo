# encoding = utf-8

from time import ctime, sleep

from myThread import MyThread

loops = [4, 2]
# 派生 Thread 的子类，并创建子类的实例
def loop(nloop, nsec):
    print('start ', nloop, 'at ', ctime())
    sleep(nsec)
    print(nloop, 'done at :', ctime())


def main():
    print('start all at :', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # 传参怎么理解?
        # 实例化的时候,除了默认参数,其他位置参数必须传递.第二个参数是一个tuple.
        # loop.__name__是什么意思
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at ', ctime())


if __name__ == '__main__':
    main()
