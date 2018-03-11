"""
功能：BMR计算器
时间：2017.12.20
"""


def main():
    a = input('是否退出程序（y/n):')
    while a != 'y':
        gender = input('请依次输入您的性别：')
        # 性别
        weight = float(input('请输入您的体重（kg）：'))
        height = float(input('请输入您的身高（cm）：'))
        age = int(input('请输入您的年龄：'))

        if gender == '男':
            bmr = (13.7*weight) + (5.0*height) - (6.8 * age) + 66
        elif gender == '女':
            bmr = (9.6*weight) + (1.8*height) - (4.7*age) +655
        else:
            bmr = -1

        if bmr !=-1:
            print('基础代谢率为(大卡）：',bmr)
        else:
            print('暂不支持该性别的bmr的运算')
        print('********************************')
        a = input('是否退出程序（y/n):')

if __name__ == '__main__':
    main()





















