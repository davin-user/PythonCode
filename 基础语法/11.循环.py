# Python中的循环有两种，一种是是for...in, 一种是while循环
"""
1.for...in循环
"""
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 计算list中每个元素之和
sum_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for n in sum_list:
    total += n
print(total)

# 求和1-100
# range()函数可以生成一个整数序列，然后在通过list函数转换为list
init_list = range(101)
print(init_list)
end_list = list(range(101))
print(end_list)
total_value = 0
for n in end_list:
    total_value += n
print(total_value)

"""
2.while循环：只要条件满足就循环，否则退出循环
"""
# 计算0-100的奇数之和
odd_sum = 0
n = 99
while n > 0:
    odd_sum += n
    n -= 2
print(odd_sum)

# 练习
L = ['Bart', 'Lisa', 'Benjamin']
for n in L:
    print(f'Hello, {n}!')

"""
3.break和continue语句
break:提前退出循环
continue:跳过本次循环，进行下一次循环
"""

n = 1
while n < 100:
    if n > 11:
        break
    print(n)
    n += 1
print('END')

m = 0
while m < 100:
    m += 1
    if m % 2 == 0:
        continue
    print(m)
print('END M')

"""
总结：3.1 break和continue语句通常要配合if语句一起使用
3.2 break和continue语句通常会造成代码执行逻辑分叉过多容易出错，大多数循环用不到break和continue语句
"""
