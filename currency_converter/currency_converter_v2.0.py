'''
作者：
功能
版本：2.0
日期
新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
'''
# 汇率
USD_VS_RMB = 6.77
current_str_value = input('请输入带单位的货币金额：(Q是退出）')
while current_str_value!='Q':
    # 获取货币单位
    unit = current_str_value[-3:]
    num = eval(current_str_value[:-3])
    # print(num)
    # print(unit)
    unit = unit.lower()
    if unit == 'rmb':
        usd_value = num/USD_VS_RMB
        print('兑换的金额是%sUSD'%usd_value)
    elif unit == 'usd':
        rmb_value = num * USD_VS_RMB
        print('兑换的金额是%sRMB'%rmb_value)
    else:
        print('您输入的金额有误')
    print('**************************************************')
    current_str_value = input('请输入带单位的货币金额：(Q是退出）')



