"""
功能：判断第几天,使用列表实现
"""

from _datetime import datetime

def is_leap_year(year):
    """
    判断year是否为闰年
    是，返回true
    否， 返回false
    """
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap

def main():

    input_date_str = input('请输入日期（yyy-mm-dd):')
    input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
    week_num = input_date.isocalendar()[1]
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    days = 0
    days += day
    month_day = {1:31,
                 2:28,
                 3:31,
                 4:30,
                 5:31,
                 6:30,
                 7:31,
                 8:31,
                 9:30,
                 10:31,
                 11:30,
                 12:31}


    for i in range(1,month):
        days += month_day[i]

    if is_leap_year(year)and month>2:
        days += 1


    print('这是{}年的第{}天，是第{}周'.format(year,days,week_num))


if __name__ == '__main__':
    main()
