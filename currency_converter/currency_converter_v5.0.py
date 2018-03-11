

'''
作者：
功能
版本：2.0
日期
新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
'''
USD_VS_RMB = 6.77


def converter(money,rate):
    return money * rate


current_str_value = input('请输入带单位的货币金额：(Q是退出）')

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
    a = converter(num,USD_VS_RMB)
    print(a)
else:
    print('不支持该货币')








