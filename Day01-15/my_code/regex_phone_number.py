import re

def get_phone_number_list(str):
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')

    # 将结果存入列表
    phone_list = re.findall(pattern, str)
    print(phone_list)
    
    #通过迭代器遍历所有结果
    for temp in pattern.finditer(str):
        print(temp.group())

    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(str)
    while m:
        print(m.group())
        m = pattern.search(str, m.end())

def main():
    sentence = '''
重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也是110或119，王大锤的手机号才是15600998765。
'''
    get_phone_number_list(sentence)


if __name__ == '__main__':
    main()