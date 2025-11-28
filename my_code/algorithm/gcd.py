# Greatest Common Divisor
# 辗转相除法
# 辗转相除法基于如下原理：两个整数的最大公约数等于其中较小的数和两数相除余数的最大公约数 gcd(a,b) = gcd(b,a mod b)
def get_gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return get_gcd(num2, num1%num2)

'''
为什么 b 和 r 的公约数集合 = a 和 b 的公约数集合？

因为：
a=q⋅b+r
如果一个数能整除 b 和 r，它一定能整除 a（因为它能整除 q·b 和 r）。
反过来，如果一个数能整除 a 和 b，它也能整除 r（因为 r = a - q·b）。
所以公约数集合在 (a, b) 和 (b, r) 之间保持一致。
'''




if __name__ == "__main__":
    print(get_gcd(6,12))
