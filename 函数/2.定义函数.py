# 1. Python中定义一个函数使用def语句，然后在缩进块中编写语句，返回值用return语句返回

# 示例1： 定义一个绝对值的函数

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-100))


# 如果没有return语句，函数执行完以后也会返回结果，只是结果为None。return None也可以简写为return


# 2.空函数：如果定义一个函数什么都不做，就可以使用pass语句，实际上pass就是一个占位符，作用就是先让函数运行起来
def nop():
    pass


# 另外pass还可以在其它语句里
# 缺少了pass，代码运行就会报错
age = 16
if age >= 18:
    pass


# 3.参数检查
# 3.1 如果调用函数时，参数个数不对，Python解释器会自动检查出来，并抛出TyperError错误

# print(my_abs(age, 19))  # TypeError: my_abs() takes 1 positional argument but 2 were given

# 3.2 如果调用函数时，如果参数类型不对，则定义的函数Python解释器无法检查，但是内置函数就可以

# print(my_abs('123'))  # 什么也不会输出
# print(abs('123'))  # TypeError: '>=' not supported between instances of 'str' and 'int'


# 完善当前的绝对值函数
def end_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('operand must be int or float')
    if x >= 0:
        return x
    else:
        return -x


# print(end_abs('123'))  # TypeError: operand must be int or float


# 3.3 函数也可以返回多个值
# 示例：游戏中从一个坐标点移动到另一个坐标点，给出坐标，位移和角度
import math


def move(x, y, step, angle=0.0) -> tuple[float, float]:
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 4)
print(f'位移后的坐标是:({r[0]:.2f},{r[1]:.2f})')
