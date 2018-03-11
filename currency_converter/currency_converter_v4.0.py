

'''
作者：
功能
版本：2.0
日期
新增功能：让程序结构化，简单函数的定义
'''


# 主函数
def main():
    USD_VS_RMB = 6.77
    current_str_value = input('请输入带单位的货币金额：')

    # 获取货币单位
    unit = current_str_value[-3:]

    # print(num)
    # print(unit)
    unit = unit.lower()

    if unit == 'rmb':
        USD_VS_RMB = 1/USD_VS_RMB
    elif unit == 'usd':
        USD_VS_RMB = USD_VS_RMB
    else:
        USD_VS_RMB = -1

    if USD_VS_RMB != -1:
        num = eval(current_str_value[:-3])
        converter2 = lambda money: money * USD_VS_RMB
        print('兑换完的货币金额：'+converter2(num))

        # a = converter(num,USD_VS_RMB)
        # print(a)
    else:
        print('不支持该货币')


if __name__ == '__main__':
    main()





