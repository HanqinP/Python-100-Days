import os
import time

def scrolling_text():
    content = "上海欢迎您....."

    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    scrolling_text()