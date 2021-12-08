# o キーボードから、「a」または「b」を選択する
#  空文字の時は終了する
#  選択肢以外の場合は、再入力
# o 選択に応じて、実行するプログラムを切り替える。
#  ただし、if を使わずに切り替えたい。（関数を辞書に格納して利用しよう）
# 【実行例】
# a=>Hello,b=>Goodbye
# どちらを実行しますか？:a
# Hello
# a=>Hello,b=>Goodbye
# どちらを実行しますか？:b
# Goodbye
# a=>Hello,b=>Goodbye
# どちらを実行しますか？:c
# どちらかを選択してください。
# a=>Hello,b=>Goodbye
# どちらを実行しますか？:
# 8
# 【select_func.py】


# 関数を辞書で渡し、実行する
def func1():
    print("Hello")


def func2():
    print("Goodbye")


# main
run_list = {'a': func1, 'b': func2}

while True:

    select = input('どちらを実行しますか？')
    # p.104 制御構文について
    if select == "":
        break

    if select in run_list.keys():  # run_list(辞書)のkeyに入力値が存在する場合
        run_list[select]()
    else:
        print("どちらかを選択してください。")


print(run_list.keys())  # dict_keys(['a','b'])
