"""
功能52周存钱挑战
"""
import math

def save_money(money_per_week,increase_money,total_week):
    money_list = []
    for i in range(total_week):
        money_list.append(money_per_week)
        print('第{}周  存入{}元  账户累计{}元 '.format(i + 1, money_per_week, math.fsum(money_list)))
        money_per_week += increase_money

def main():
    print('请输入以下内容，使用空格隔开。')
    money = input('每周存入的金额  每次递增的金额  总共的周数：')
    L = money.split(' ')

    money_per_week = eval(L[0]) # 每周存入的金额
    increase_money = eval(L[1])  # 递增的金额
    total_week = int(L[2])       # 总共的周数

    save_money(money_per_week,increase_money,total_week)


if __name__ == '__main__':
    main()










