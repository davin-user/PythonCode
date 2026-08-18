"""
int(x) 将x转换为整形
float(x) 将x转换为浮点型
str(x) 将x转换为字符串
"""
# 任何类型都可以转换为字符串
# 字符串内必须要有数字才能转换为数字类型

change_int_value = int('123')
change_float_value = float(123)
change_str_value = str(123)
print(type(change_int_value))
print(change_float_value)
print(type(change_float_value))
print(type(change_str_value))