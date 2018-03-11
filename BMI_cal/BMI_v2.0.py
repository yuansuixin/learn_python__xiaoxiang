"""
功能：BMR计算器
时间：2017.12.20
"""


def main():
    a = input('是否退出程序（y/n):')
    while a != 'y':
        print('请输入以下信息，使用空格隔开')
        input_str = input('性别、体重（kg）、身高（cm）、年龄：')
        L = input_str.split(' ')

        gender = L[0]
        weight = float(L[1])
        height = float(L[2])
        age = int(L[3])

        if gender == '男':
            bmr = (13.7*weight) + (5.0*height) - (6.8 * age) + 66
        elif gender == '女':
            bmr = (9.6*weight) + (1.8*height) - (4.7*age) +655
        else:
            bmr = -1

        if bmr !=-1:
            # print('基础代谢率为%.2f卡路里！'% bmr)
            print('您的性别：{}，体重：{}，公斤，身高：{}厘米，年龄：{}岁'.format(gender,weight,height,age))
            print('您的基础代谢率为{}卡路里！'.format(bmr))
        else:
            print('暂不支持该性别的bmr的运算')
        print('********************************')
        a = input('是否退出程序（y/n):')


if __name__ == '__main__':
    main()





















