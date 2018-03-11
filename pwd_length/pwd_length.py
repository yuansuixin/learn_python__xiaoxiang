

def check_number(password):
    has_num = False
    for c in password:
        if c.isnumeric():
            has_num = True
            break
    return has_num

def check_letter(password):
    has_letter = False
    for c in password:
        if c.isalpha():
            has_letter = True
            break
    return has_letter

def main():
    try_time = 5
    while try_time>0:
        password = input('请输入密码：')

        # 密码强度
        strlength_level = 0

        # 密码长度要大于8
        if len(password) >= 8:
            strlength_level +=1
        else:
            print('密码长度要求至少8位')


        if check_letter(password):
            strlength_level +=1
        else:
            print('密码需要包含字母')


        if check_number(password):
            strlength_level +=1
        else:
            print('密码需要包含数字')



        if strlength_level == 3:
            print('密码长度合格')
            break
        else:
            print('密码长度不合格')
        print()
    if try_time<0:
        print('尝试的次数过多。')




if __name__ == '__main__':
    main()













































