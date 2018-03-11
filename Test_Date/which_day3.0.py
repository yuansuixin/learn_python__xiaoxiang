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
    # 包含30天的集合
    days_30_month = {4,6,9,11}
    days_31_month = {1,3,5,7,8,10,12}


    days = 0
    for i in range(1,month):
        if i in days_30_month:
            days+=30
        elif i in days_31_month:
            days += 31
        else:
            days+=28

    if is_leap_year(year)and month>2:
        days += 1

    days += day
    print('这是{}年的第{}天，是第{}周'.format(year,days,week_num))


if __name__ == '__main__':
    main()
