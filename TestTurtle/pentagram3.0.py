"""
功能：多个五角星的绘制
"""
import turtle


def pentagram(size):
    """
    迭代绘制五角星
    """
    if size >= 100:
        return
    else:
        for i in range(5):
            turtle.forward(size)  # 从左往右
            turtle.right(144)
        size += 10
        return pentagram(size)

def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')
    pentagram(50)


if __name__ == '__main__':
    main()




























