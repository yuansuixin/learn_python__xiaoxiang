"""
模拟投掷两个骰子，直方图
"""
import random
import matplotlib.pyplot as plt

# 更改字体，默认的字体不支持中文，改为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 更改负号的问题，
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    """
    模拟掷骰子
    :return:
    """
    roll = random.randint(1,6)
    return roll

def main():
    toal_times = 1000
    roll_list = []
    for i in range(toal_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1+roll2)

    # 直方图
    #normed概率，bins是横坐标的分割edgecolor分割线的颜色，linewidth分割线的宽度
    plt.hist(roll_list,bins=range(2,14),edgecolor='black',linewidth=1,normed=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()






