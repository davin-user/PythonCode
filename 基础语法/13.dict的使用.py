# Python内置的字典：dict使用key-value的键值对形式，有极快的查询速度
scores_dict = {
    'Michael': 90,
    'Ben': 78,
    'Tracy': 70,
    'Jackson': 90,
}
print(scores_dict['Jackson'])

# 通过指定的key，可以给字典添加值
scores_dict['Toms'] = 89
print(scores_dict['Toms'])

# 通过in或者get() 判断key是否存在
# 1.in
have_value = 'Davin' in scores_dict
print(have_value)

# 2.使用get()方法，如果不存在在返回None或者指定的值
print(scores_dict.get('Mike'))
print(scores_dict.get('CodeWars', -1))

# 3.使用pop方法删除指定的key
dele_key = scores_dict.pop('Toms')
print(dele_key)
print(scores_dict)

# 和list比较
# 查找和插入的速度极快，不会随着key的增加而变慢
# 需要占用大量的内存，内存浪费多

# list会查找和插入的事件会随着元素的增加而增加
# 占用空间小，浪费内存的要很少


"""
总结：  dict是用空间来换时间的一种方法
       dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，而且dict的key必须是不可变的对象
"""
