# o キーボードから数値を入力する。（0 で終了）
#  入力した値を元に、使用する関数を決定する choice_func()を呼び出す。
#  戻り値は、使用する関数を直接返す。
#  奇数が入力されたら odd 関数を、偶数が入力されたら even 関数を返す。
# o メイン側で、戻り値を実行する。
# 【実行例】
# > python choice.py
# 数字を入力してください。（0：終了）10
# 偶数
# 数字を入力してください。（0：終了）13
# 奇数
# 数字を入力してください。（0：終了）ab
# 入力が正しくありません
# 数字を入力してください。（0：終了）0


# 【choice.py】
def odd():
    print("奇数")


def even():
    print("偶数")


def choice_func(number):
    func_dic = {1: odd , 0: even}
    func = func_dic[number % 2]
    return func

# def choice_func2(number):
#     if number % 2 == 0:
#         func = even
#     else:
#         func = odd
#     return func

# main
while True:
    num = input("数字を入力してください。（0：終了）")
    if num.isnumeric():
        num = int(num)
    else:
        print("入力が正しくありません")
        continue
    if num == 0:
        break
    choice_func(num)()