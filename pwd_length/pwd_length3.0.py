
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
    # 判断是否含有数字
    def check_number(self):
        has_num = False
        for c in self.password:
            if c.isnumeric():
                has_num = True
                break
        return has_num
    # 判断是否含有字母
    def check_letter(self):
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


class FileTool:
    """
    文件工具类
    """

    def __init__(self,filepath):
        self.filepath = filepath

    # 写文件
    def write_to_file(self,line):
        f= open(self.filepath,'a')
        f.write(line)
        f.close()

    # 读文件
    def read_from_file(self):
        f = open(self.filepath,'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    try_time = 5
    filetool = FileTool('passwordt.txt')
    while try_time>0:
        password = input('请输入密码：')
        try_time-=1
        password_tool = PasswordTool(password)
        password_tool.process_password()

        line = '密码：{},强度：{}'.format(password,password_tool.strlength_level)+ '\n'
        # 写文件
        filetool.write_to_file(line)

        if password_tool.strlength_level == 3:
            print('密码长度合格')
            break
        else:
            print('密码长度不合格')
        print()

    if try_time<=0:
        print('尝试的次数过多。')

    # 读
    lines = filetool.read_from_file()
    print(lines)

if __name__ == '__main__':
    main()













































