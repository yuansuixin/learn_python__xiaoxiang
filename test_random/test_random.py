
import random

def roll_dice():
    """
    模拟掷骰子
    :return:
    """
    roll = random.randint(1,6)
    return roll

def main():
    toal_times = 1000
    # 列表
    result_list = [0]*6

    for i in range(toal_times):
        roll= roll_dice()
        for j in range(1,7):
            if roll == j:
                result_list[j-1] += 1
    for i,result in enumerate(result_list):
        print('点数{}的次数:{},频率：{}'.format(i+1,result,result/toal_times))

if __name__ == '__main__':
    main()






