age = 3
if age >= 18:
    print('your age is ', age)
    print('default')

if age >= 18:
    print('your age is ', age)
else:
    print('your are teenager ')

if age >= 18:
    print('your age is ', age)
elif age < 18:
    print('your are teenager')
else:
    print('default')

# if判断条件还可以简写
# 如果x是非空字符串、非0数值或者非空list，则判断为true，否则为false
# x = 1
# if x:
#     print('x')
#
# input_birth = input('Please input your birthday:')
# birth = int(input_birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# 条件判断连写
height = float(input('Please input your height(m):'))
weight = float(input('Please input your weight(kg):'))
bmi = weight / height ** 2

if bmi < 18.5:
    print('过轻', bmi)
elif 18 <= bmi < 25:
    print('正常', bmi)
elif 25 <= bmi < 28:
    print('过重', bmi)
elif 28 <= bmi < 32:
    print('肥胖', bmi)
else:
    print('严重肥胖', bmi)
