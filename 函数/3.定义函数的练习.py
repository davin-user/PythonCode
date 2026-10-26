# 定义一个函数quadratic(a,b,c),接收三个参数，返回一元二次方程的两个解：a * x * x + b * x + c = 0
import math


def quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return '无实数解'
    elif delta == 0:
        return -b / (2 * a)

    result_sqrt = math.sqrt(delta)
    x1 = (-b + result_sqrt) / (2 * a)
    x2 = (-b - result_sqrt) / (2 * a)
    return x1, x2


print('quadratic(a,b,c)=', quadratic(3, 8, 3))
