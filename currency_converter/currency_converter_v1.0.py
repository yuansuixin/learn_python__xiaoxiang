'''
作者：
功能
版本
日期

'''

rmb_str_value = input('请输入人民币（CNY）金额：')
rmb_value = eval(rmb_str_value)

USD_VS_RMB = 6.77

usd_value = rmb_value / USD_VS_RMB

print('兑换后的美元（USD）金额为：', usd_value)



















