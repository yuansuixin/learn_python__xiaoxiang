"""
功能：多个五角星的绘制
"""
import turtle


def pentagram(size):
    """
    :param size: 大小
    :return:
    """
    for i in range(5):
        turtle.forward(size)  # 从左往右
        turtle.right(144)

def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50
    while size <= 100:
        # 绘制五角星
        pentagram(size)
        size += 20
    turtle.exitonclick()


if __name__ == '__main__':
    main()




























