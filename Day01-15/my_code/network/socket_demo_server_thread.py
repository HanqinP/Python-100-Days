from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():

    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    
    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('localhost',5566))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open(r'Day01-15\my_code\network\guido.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        '''
        一：为什么要使用base64格式传输文件？
        通常我们在使用服务的时候，数据从我们的设备传输到服务器，往往会有两种方式：一是直接传输文件，但这种情况受网络情况影响较大，文件可能传不过去，并且文件直接在网路上传播，你的数据安全就保证不了。因此需要一种加密格式，也就是我们使用的第二种方法，base64格式加密。有对base64算法加密的过程感兴趣的推荐看一下这一篇博客：

        https://blog.csdn.net/robertcpp/article/details/51628647

        对base64的编码转码都有比较详细的介绍。

        简单来说就是把一张图片数据加密成一串字符，使用该字符串代替图像地址。

        个人觉得，使用base64可以带来以下优点

        1.减少了HTTP请求
        .某些文件可以避免跨域的问题
        3.避免了图片更新时要重新上传，还要清理缓存的问题
        '''
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()