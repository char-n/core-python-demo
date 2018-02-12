# encoding=utf-8

import threading
from time import ctime, sleep


# 方式一：创建 Thread 的实例，传给它一个函数

loops = [4, 2]


def loop(nloop, nsec):
    print('start loop ', nloop, 'at :', ctime())
    sleep(nsec)
    print('loop', nloop, ' done at :', ctime())


def main():
    print('start all at :', ctime())
    threads = []

    nloops = range(len(loops))

    for i in nloops:
        thread = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(thread)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()




if __name__ == '__main__':
    main()
