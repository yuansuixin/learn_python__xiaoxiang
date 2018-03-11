
## 绘制分型树

import turtle


def draw_brach(brach_length):
    if brach_length > 5:
        # 绘制右侧的树枝
        turtle.forward(brach_length)
        print('向前',brach_length)
        turtle.right(20)
        print('右转20')
        draw_brach(brach_length-15)

        # 绘制左侧的树枝
        turtle.left(40)
        print('左转40')
        draw_brach(brach_length-15)

        # 返回之前的树枝上
        turtle.right(20)
        print('右转20')
        turtle.backward(brach_length)
        print('返回',brach_length)


def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color('red')

    draw_brach(100)


    turtle.exitonclick()




if __name__ == '__main__':
    main()












