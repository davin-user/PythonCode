# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以在set中没有重复的key

# 使用set创建
my_list = [1, 2, 3, 4, 5, 6]
default_set = set(my_list)
print(default_set)
# 注意： 传入的参数是[1, 2, 3, 4, 5, 6],而显示的是{1, 2, 3, 4, 5, 6},只是告诉你set内部有{1, 2, 3, 4, 5, 6}这6个元素
# 而且显示的顺序也不表示set内部就是有序的

# 使用集合字面量创建
first_item = {5, 6, 7}
print(first_item)

# 可以通过add(key)方法向set内部添加元素，可以重复添加但是不会有效果
first_item.add(8)
first_item.add(9)
first_item.add(9)
print(first_item)

# 可以通过remove(key)方法删除元素
first_item.remove(9)
print(first_item)

# set可以看成数学意义上的无序和无重复元素的集合，所以也可以进行数学意义上的交集和并集操作
end_list = default_set & first_item
print(end_list)

end_list1 = default_set | first_item
print(end_list1)

# 不可变对象
# str是不可变对象，list是可变对象
test_list = [4, 2, 4, 1, 2, 6]
test_list.sort()
print(test_list)  # [1, 2, 2, 4, 4, 6]

test_str = 'abc'
result = test_str.replace('a', 'A')
print(test_str)  # abc
print(result)  # Abc

# 使用key-value存储的dict在Python中非常有用，选择不可变对象很重要，而最常用的key就是字符串
