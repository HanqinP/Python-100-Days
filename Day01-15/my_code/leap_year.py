# 闰年
# 计算当前日期是一年里的第几天
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, day):
    month_list = [[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]][is_leap_year(year)]
    days = 0
    for index in range(month):
        days += month_list[index]

    return days


if __name__ == '__main__':
    res = which_day(2025, 3, 25)
    print(res)