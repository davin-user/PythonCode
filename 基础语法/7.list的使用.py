# 1.list是一种有序的集合，可以随时添加和删除元素
classmates = ['Mike', 'Bob', 'Alice']

# 1.1 使用len获取list元素的个数
length = len(classmates)
print(length)

# 1.2 使用索引获取集合中每个位置的元素
print(classmates[0])

# 1.3 如果索引超出范围，会报一个IndexError错误
# 获取集合中最后一个元素一般使用len(classmates)-1 或者是 classmates[-1]
# print(classmates[3])
print(classmates[-1])

# 1.4 list是一个可变的有序表，可以添加，插入和删除元素
# 1.4.1 末尾追加一个元素
classmates.append('Jerry')
print(classmates)

# 1.4.2 插入一个元素
classmates.insert(1, 'Tom')
print(classmates)

# 1.4.3 删除末尾元素
classmates.pop()
print(classmates)

# 1.4.4 删除指定位置的元素
pop_value = classmates.pop(2)
print(pop_value)
print(classmates)

# 1.4.5 把某个元素替换成别的值
classmates[0] = 'Davin'
print(classmates)

# 1.5 list 元素可以是另一个list
courses = ['Math', 'English', ['Python', 'Java', 'JavaScript'], 'History', 'French']
print(courses)
print(courses[2][0])
