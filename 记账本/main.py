# 记账本 v1 —— 主线练习项目
#
# 【数据结构】一条记录是一个 dict：
#     {'date': '2026-09-10', 'category': '吃饭', 'amount': 35.5, 'note': '午饭'}
# 所有记录放在一个 list 里：records = [记录1, 记录2, ...]
#
# 【当前要求】下面 6 个函数的函数体是空的（pass），
# 等你学完「函数」那一章，把它们的实现补上。
# main() 已经写好了，它就是「调用方」，你写完后直接运行就能用。
#
# 【基础语法知识点落位】这个项目用到了你学过的：
#   变量 / 类型转换 / 输入输出 / list / dict / set / 条件判断 / 循环 / 模式匹配
#   其中「模式匹配」用在 main() 里，「set」用在 list_categories 里，
#   「type / isinstance」用在 get_total 里
#
# 【后续改造计划】学到对应章节再回来改，不要提前做：
#   高级特性    → 用列表推导式 / 字典推导式替换现在的朴素循环
#   函数式编程  → sorted 按金额排序、filter 筛选
#   面向对象    → 把 dict 记录改成 Record 类
#   错误处理    → 输入加 try/except，金额输入非数字不能崩
#   文件 IO     → 存成 JSON，关掉程序数据还在
#   模块        → 拆成 main.py + storage.py + models.py
#   测试        → 给 get_total 这类纯函数补 assert

records = []  # 所有记录都存在这个 list 里

# ---------------------------------------------------------------------------


def show_menu():
    """打印菜单，返回用户选择的编号（字符串）。

    期望打印成这样：
        1. 记一笔
        2. 查看全部
        3. 看总额
        4. 看类别
        5. 删除一笔
        6. 退出

    提示：用 print 打印，最后用 input('请选择：') 拿到用户输入并 return。
    """
    pass


def add_record(records):
    """让用户输入 日期 / 类别 / 金额 / 备注，组装成一条 dict，追加到 records。

    要求：
      - 日期可以不填，不填就存空字符串 ''
      - 金额要用 float() 转成数字再存
      - 提示：dict 的写法是 {'date': ..., 'category': ..., 'amount': ..., 'note': ...}
    """
    pass


def list_records(records):
    """打印所有记录，每条一行，编号从 1 开始（用 enumerate 或自己加计数器）。

    要求：
      - 如果 records 是空的，打印「还没有任何记录」并直接 return
      - 建议用 f-string 对齐，例如：
            print(f'{i}. {r["date"]}  {r["category"]}  {r["amount"]}  {r["note"]}')
    """
    pass


def get_total(records):
    """返回所有记录金额之和（一个数字），不要在这里 print。

    要求：
      - 先 total = 0，然后 for 循环累加 r['amount']，最后 return total
      - 累加前先确认这个金额真的是数字，不是数字就跳过（防止数据被写坏）：
            if not isinstance(r['amount'], (int, float)):
                continue
        注意 isinstance 第二个参数写成元组 (int, float)，表示「是其中任意一种就行」
    """
    pass


def list_categories(records):
    """打印出目前记过的所有类别，重复的只显示一次。

    提示：类别去重正是 set 的用途。你现在还没学推导式，用最朴素的办法：
        先建一个空的 set()，然后 for 循环遍历 records，用 .add() 把 r['category'] 加进去
        最后打印出来
      - 如果 records 是空的，打印「还没有任何记录」并直接 return
    """
    pass


def delete_record(records):
    """按编号删除一条记录。编号就是 list_records 里显示的那个 1、2、3...

    要求：
      - 先让用户输入编号
      - 用 int() 把输入转成数字
      - 编号范围是 1 ~ len(records)，对应的 list 下标是「编号 - 1」
      - 删掉之后打印提示，比如「已删除」
    """
    pass


# ---------------------------------------------------------------------------


def main():
    """主循环：显示菜单 → 分发到对应函数 → 直到用户选退出。"""
    while True:
        choice = show_menu()
        match choice:
            case '1':
                add_record(records)
            case '2':
                list_records(records)
            case '3':
                print(f'总支出：{get_total(records)}')
            case '4':
                list_categories(records)
            case '5':
                delete_record(records)
            case '6':
                print('再见！')
                break
            case _:
                print('没有这个选项，请重新选择')


main()
