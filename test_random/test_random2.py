"""
模拟投掷两个骰子
"""
import random
import matplotlib.pyplot as plt

def roll_dice():
    """
    模拟掷骰子
    :return:
    """
    roll = random.randint(1,6)
    return roll

def main():
    toal_times = 100
    # 列表
    result_list = [0]*11
    # 点数列表
    roll_list = list(range(2,13))
    roll_dict = dict(zip(roll_list,result_list))

    # 记录第一个骰子的结果
    roll1_list = []
    roll2_list= []


    for i in range(toal_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)
        for j in range(2,13):
            if roll1+roll2 == j:
                roll_dict[j] += 1
    for i,result in roll_dict.items():
        print('点数{}的次数:{},频率：{}'.format(i,result,result/toal_times))


    # 数据的可视化
    # 散点图
    x = range(1,toal_times+1) # 次数
    plt.scatter(x,roll1_list,alpha=0.5,c='red')
    plt.scatter(x, roll2_list, alpha=0.5,c='green')
    plt.show()



if __name__ == '__main__':
    main()






