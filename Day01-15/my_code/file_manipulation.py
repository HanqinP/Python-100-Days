import time


def file_read(path):
    with open(path, 'r') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.2)

def file_write(path, content):
    with open(path, 'w') as f:
        f.write(content)

def image_read(path):
    with open(path, 'rb') as f:
        return f.read()
    
def image_copy(path, buffer):
    with open(path, 'wb') as f:
        f.write(buffer)

def main():
    try:
        # 读文件
        file_read(r'file1.txt')
        print()

        # 写文件
        file_write(r'file2.txt', "Hello world! This is file2")

        # 读写二进制文件（图片的读取和复制）
        buffer_image = image_read(r'ball.png')
        image_copy(r'ball_copy.png', buffer_image)

    except FileNotFoundError:
        print('file not found')
    except LookupError:
        print('unknown encoding')
    except UnicodeDecodeError:
        print('decode error')
    except IOError:
        print('write to the file error')
    
if __name__ == '__main__':
    main()