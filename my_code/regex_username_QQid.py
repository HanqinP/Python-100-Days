import re

def main():
    username = input("请输入用户名：")
    qq = input('请输入QQ号：')
    pattern_username = re.compile(r'^\w{6,20}$')
    m1 = re.match(pattern_username, username)
    res_m1 = m1.group(0)
    print(res_m1)
    if not m1:
        print('请输入有效的用户名')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号')
    

if __name__ == '__main__':
    main()