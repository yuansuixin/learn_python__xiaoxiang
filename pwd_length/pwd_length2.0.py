




class PasswordTool:
    """
    密码工具类
    """
    def __init__(self,password):
        self.password = password
        self.strlength_level = 0

    def process_password(self):
        # 密码长度要大于8
        if len(self.password) >= 8:
            self.strlength_level += 1
        else:
            print('密码长度要求至少8位')

        if self.check_letter():
            self.strlength_level += 1
        else:
            print('密码需要包含字母')

        if self.check_number():
            self.strlength_level += 1
        else:
            print('密码需要包含数字')

    def check_number(self):
        has_num = False
        for c in self.password:
            if c.isnumeric():
                has_num = True
                break
        return has_num

    def check_letter(self):
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

def main():
    try_time = 5
    while try_time>0:
        password = input('请输入密码：')
        try_time-=1
        password_tool = PasswordTool(password)

        password_tool.process_password()

        with open('password.txt', 'a') as f:
            f.write('密码：{},强度：{}'.format(password,password_tool.strlength_level)+ '\n')

        if password_tool.strlength_level == 3:
            print('密码长度合格')
            break
        else:
            print('密码长度不合格')
        print()

    if try_time<=0:
        print('尝试的次数过多。')


if __name__ == '__main__':
    main()













































