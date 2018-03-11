"""
功能52周存钱挑战
"""
import math

def main():
    money_per_week = 10 # 每周存入的金额
    i = 1               # 记录周数
    increase_money = 10  # 递增的金额
    total_week = 52       # 总共的周数


    money_list = []
    for i in range(total_week):
        money_list.append(money_per_week)
        print('第{}周  存入{}元  账户累计{}元 '.format(i+1, money_per_week, math.fsum(money_list)))
        money_per_week += increase_money

if __name__ == '__main__':
    main()










