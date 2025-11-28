from random import randint
from threading import Thread
from time import time, sleep

'''
这里使用多线程的继承来实现
'''
class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        download(self._filename)

def download(filename):
    print('start to download%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('finish to download%s! Cost %ds' %(filename, time_to_download))

'''
这里直接使用multithread类里的Thread类来创建多线程
'''
def download_with_multithread():
    start = time()
    t1 = Thread(target=download, args=('Python.pdf', ))
    t1.start()
    t2 = Thread(target=download, args=('Java.pdf', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('Totally cost%.3fs' % (end-start))

'''
这里继承多线程mutithread的Thread类来实现
'''
def download_with_multithread_inheritance():
    start = time()
    t1 = DownloadTask('Python.pdf')
    t1.start()
    t2 = DownloadTask('Java.pdf')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('Totally cost %.2fs' %(end - start))

if __name__ == '__main__':
    #download_with_multithread()

    download_with_multithread_inheritance()