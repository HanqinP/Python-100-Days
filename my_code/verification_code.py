import random


def generate_verification_code(n: int):
    str = '1234567890qwertyuiopasdfghjklzxcvbnm'
    str_length = len(str)
    res = ''
    for _ in range(n):
        seed = random.randint(0,str_length-1) #Return random integer in range [a, b], including both end points.
        res += str[seed]

    return res


if __name__ == '__main__':
    print(generate_verification_code(4))