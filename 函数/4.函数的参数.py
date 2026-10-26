# 1.位置参数：调用函数的时候，传入的值按照位置顺序一次赋值给参数
# def power(x):
#     return x * x
#
#
# print(power(2))


def power(x: int, n: int):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s


print(power(2, 3))


# 2.默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s


# 使用默认参数注意事项
# 1.1 必选参数必须在前，默认参数在后，否则Python解释器会报错
# 1.2 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面，其中变化小的参数就可以作为默认参数
# 1.3 使用默认参数的最大好处就是可以降低函数调用难度

# 例如下面的例子：
def enroll(name: str, gender: str, age: int = 6, city: str = 'shanghai'):
    print(name)
    print(gender)
    print(age)
    print(city)
    return f'{name} {gender} {age} {city}'


print(enroll('g', '男'))

# 1.4 调用的时候即可以按照顺序传递默认参数，也可以不按照顺序传递参数

print(enroll('uly', '男', 6))
print(enroll('gly', '男', city='shanghai'))


# 1.5 默认参数的坑
def append_end(l=[]):
    l.append('end')
    return l


print(append_end())  # ['end']
print(append_end())  # ['end', 'end']
print(append_end())  # ['end', 'end', 'end']


# 原因： Python函数在定义的时候，默认参数l的值就已经被算出来,即[]
# 因为默认参数l也是一个变量，指向对象[],每次调用该函数，如果改变了l的内容，则下次调用的时候，默认参数的内容就变了，不在是定义时的[]
# 注意：因此定义默认参数的时候，必须指向不变的对象

# 重新修改上面的例子
def update_append(l=None):
    if l is None:
        l = []
    l.append('end')
    return l


print(update_append())
print(update_append())
print(update_append())
print(update_append())
