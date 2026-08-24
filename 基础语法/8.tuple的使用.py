# tuple元组一种有序列表
# 和list不同的是一旦初始化就不能修改了

classmates = ('Bob', 'Mike', 'Tom')
print(classmates)
# 因为tuple不可变，所以相对更安全。如果可能能使用tuple尽量使用tuple
# 注意：所谓的不变是指的指向不变。即指向‘a’就不能指向‘b’,指向一个list就不能改成指向其它对象，但是指向的这个list本身是可变的
t = ('Tom', 'Jerry', ['123', '12313'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# 获取tuple中的元素
name = classmates[0]
print(name)

# 定义一个空的tuple
# roommates = ()

# 定义一个元素的tuple，后面必须使用,
roommates = ('Davin',)
print(roommates)
