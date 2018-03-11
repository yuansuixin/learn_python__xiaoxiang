"""
功能52周存钱挑战
"""
import math
import datetime

def save_money(money_per_week,increase_money,total_week):
    money_list = []
    saving_money_list = []
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saving_money_list.append(saving)
        # print('第{}周  存入{}元  账户累计{}元 '.format(i + 1, money_per_week,saving ))
        money_per_week += increase_money

    return saving_money_list

def main():
    print('请输入以下内容，使用空格隔开。')
    money = input('每周存入的金额  每次递增的金额  总共的周数：')
    L = money.split(' ')

    money_per_week = eval(L[0]) # 每周存入的金额
    increase_money = eval(L[1])  # 递增的金额
    total_week = int(L[2])       # 总共的周数

    save_money_list = save_money(money_per_week,increase_money,total_week)

    date_str = input('请输入日期（yyyy/mm/dd）：')
    # print(date_str)
    input_date = datetime.datetime.strptime(date_str,'%Y/%m/%d')
    week_num = input_date.isocalendar()[1]
    print('第{}周的存款是{}元'.format(week_num,save_money_list[int(week_num)-1]))


if __name__ == '__main__':
    main()










