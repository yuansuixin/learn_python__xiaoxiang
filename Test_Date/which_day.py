"""
功能：判断第几天
"""

from _datetime import datetime


def main():
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30)

    input_date_str = input('请输日期（yyy-mm-dd):')
    input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # print(days)
    # 计算之前月份的天数总和，以及当前月份天数
    days = sum(days_in_month[:month - 1]) + day

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        if month > 2:
            days += 1
    print('这是{}年的第{}天'.format(year,days))


if __name__ == '__main__':
    main()
