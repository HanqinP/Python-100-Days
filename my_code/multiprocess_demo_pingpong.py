'''
这是一个反面案例，演示了多进程运行同一个任务下不
适用通讯的话公共资源无法共享从而出错的案例
'''

from multiprocessing import Process
from time import sleep


counter = 0

def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)

def main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('pong', )).start()


if __name__ == '__main__':
    main()
