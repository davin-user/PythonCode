# 调用函数

# 1.求绝对值abs
test_a = abs(-100)
print(test_a)

# 调用函数如果传入的参数个数和类型不正确，则Python会报TypeError的错误
# test_b = abs(100, 2)
# print(test_b) # TypeError: abs() takes exactly one argument (2 given)


# test_c = abs('abx')
# print(test_c)  # TypeError: abs() takes exactly one argument (2 given)

test_max = max(-100, 0)
print(test_max)
test_min = min(-100, 0)

# 还有常见的内置函数如数据类型转换int(),float(),str(),bool()


# 总结：函数名其实就是指向一个函数对象的引用，完全可以把函数名赋值给一个变量，相当于给这个函数起了一个‘别名’
abs_alia = abs  # 变量abs_alia指向了abs函数
alia_value = abs_alia(-100)  # 所以也可以通过abs_alia调用abs函数
print(alia_value)

# 练习：转换成十六进制
n1 = 100
n2 = 500
print(f'n1的十六进制：{hex(n1)}\nn2的十六进制：{hex(n2)}')
