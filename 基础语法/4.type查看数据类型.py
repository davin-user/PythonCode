"""
type()查看变量类型，可以是字面量，也可以是变量
"""

# 查看字面量
print(type(123))
print(type(123.123))
print(type("查看字面量"))

print("----------------")

# 查看变量
int_value = 123
float_value = 123.45
str_value = "查看字面量类型"
print(type(int_value))
print(type(float_value))
print(type(str_value))

# 使用\转义'或者"
print('I\'m "ok"!')
# 布尔值
print(True and True)
print(True and False)
print(True or False)
print(not True)
print(not False)
