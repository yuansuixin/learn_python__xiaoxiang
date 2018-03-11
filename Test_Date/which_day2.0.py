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
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]

    input_date_str = input('请输入日期（yyy-mm-dd):')
    input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
    week_num = input_date.isocalendar()[1]
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    if is_leap_year(year):
        days_in_month[1] = 29
    # print(days)
    # 计算之前月份的天数总和，以及当前月份天数
    days = sum(days_in_month[:month - 1]) + day
    print('这是{}年的第{}天，是第{}周'.format(year,days,week_num))


if __name__ == '__main__':
    main()
