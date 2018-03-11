"""
模拟投掷两个骰子，使用科学计算库简化程序
"""
import matplotlib.pyplot as plt
import numpy as np

# 更改字体，默认的字体不支持中文，改为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 更改负号的问题，
plt.rcParams['axes.unicode_minus'] = False

def main():
    toal_times = 1000
    # 记录骰子结果
    roll1_str = np.random.randint(1, 7, size=toal_times)
    roll2_str = np.random.randint(1, 7, size=toal_times)
    result_arr = roll1_str + roll2_str

    # 拿到数据
    hist,bins = np.histogram(result_arr,bins=range(2,14))
    print(hist)
    print(bins)

    # 直方图
    # normed概率，bins是横坐标的分割edgecolor分割线的颜色，linewidth分割线的宽度rwidth方形的宽度
    plt.hist(result_arr, bins=range(2, 14), edgecolor='black', linewidth=1, normed=1,rwidth=0.8)

    # 改变横坐标的点数显示
    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) +0.5
    plt.xticks(tick_pos,tick_labels)

    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()


if __name__ == '__main__':
    main()
