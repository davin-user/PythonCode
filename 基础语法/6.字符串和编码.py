# 格式化字符串
print('hello, %s' % 'world')

print('Hi,%s,you have $%d.' % ('mike', 1000))

# 说明：% 运算符就是用来格式化字符串的
# 在字符串内部， %s表示用字符串替换 %d 表示用整数替换 %f表示用浮点数替换 %x表示用十六进制替换
# 有几个%? 占位符，后面就跟几个变量或者值，并且顺序要一一对应，如果只有一个%?,()可以省略


# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 如果字符串已经有一个%，则使用%%进行转义
print('growth rate: %d%%' % 7)

# format也能用来格式化字符串，它传入的参数依次替换字符串内部的占位符{0} {1}
print('hello {0},成绩提升了 {1:.1f}%'.format('mike', 30.125))

# f-string，它和普通字符串不同之处在于，字符串如果包含{XXX}，就会以对应的变量替换
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
# The area of a circle with radius 2.5 is 19.62


# 字符串替换的练习
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
# print(f'小明同学的成绩提升了{r:.1f}%')
# print('{0}同学成绩提升了{1:.1f}%'.format('小明', r))
print('%s同学成绩提升了%.1f%%' % ('小明', r))
