# Greatest Common Divisor
# 辗转相除法
# 辗转相除法基于如下原理：两个整数的最大公约数等于其中较小的数和两数相除余数的最大公约数 gcd(a,b) = gcd(b,a mod b)
def get_gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return get_gcd(num2, num1%num2)






if __name__ == "__main__":
    print(get_gcd(6,12))
