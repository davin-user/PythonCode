# 当我们使用if...elif...elif...elif...else的时候，代码较长可读性变差
# 因此可以使用模式匹配 match ... case ...语句

# score = float(input('Please input your score:'))
# if score >= 90:
#     print('your level is A')
# elif score >= 80:
#     print('your level is B')
# elif score >= 70:
#     print('your level is C')
# else:
#     print('your level is D')


# 1.使用_表示匹配到其它任何情况
# grade = input('Please input your grade:')
# match grade:
#     case 'A':
#         print('your grade is A')
#     case 'B':
#         print('your grade is B')
#     case 'C':
#         print('your grade is C')
#     case 'D':
#         print('your grade is D')
#     case _:
#         print('your grade is 0')


# 2.复杂匹配
# match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定的范围，并且将匹配后的值绑定到变量
# age = int(input('please input your age:'))
# match age:
#     case x if x < 10:
#         print(f' < 10 years old: {x}')
#     case 10:
#         print('10 years old')
#     case 11 | 12 | 14 | 15 | 16 | 17 | 18 | 19 | 20:
#         print('11~20 years old')
#     case _:
#         print('not sure')

# 3.匹配列表
# 场景：用户输入一个命令,用args = ['gcc','hello.c','world.c']存储，使用match来匹配解析这个列表
args = ['gcc', 'hello.c', 'world.c']
match args:
    # 如果只出现gcc，报错
    case ['gcc']:
        print('gcc:missing source file(s)')
    # 出现gcc,且至少指定一个文件
    case ['gcc', file1, *files]:
        print('gcc compile:' + file1 + ',' + ',' + '.join(files)')
    # 仅出现clean
    case ['clean']:
        print('clean')
    case _:
        print('invalid command')
