# o 関数、do_anything( )を作成する
# o 引数がない場合は、「やること無いので暇です」と表示
# o 引数が 1 個の場合
#  文字列なら、受け取った文字列を 2 回表示する
#  数値なら、2 倍した値を表示する
#  それ以外は、「難しくて無理です」と表示
# o 引数が 2 個の場合
#  数値どうしなら、足した結果を表示する
#  文字列同士なら、文字列を結合した結果を表示する
#  異なる型なら、「できません〜」と表示する
#  数値、文字列以外なら、「無茶言わないで！」と表示する
# o 引数が 3 個以上の場合
#  「無理です…」と表示する

# 【実行結果】
# > python func_3.py
# 受け取った値：()
# やること無いので暇です
# 7
# 受け取った値：(10,)
# 20
# 受け取った値：('asdfg',)
# asdfgasdfg
# 受け取った値：([1, 2, 3],)
# 難しくて無理です
# 受け取った値：(10, 20)
# 30
# 受け取った値：(10, 'abc')
# できません〜
# 受け取った値：('x', 'yz')
# xyz
# 受け取った値：([1, 2, 3], [4, 5, 6])
# 無茶言わないで！
# 受け取った値：(1, 2, 3)
# 無理です...

# 【func_3.py】
def do_anything(*args):
    # args 受け取った値は、タプルとなる。
    '''引数の個数によって何かする。int と str で動作'''
    print(f'受け取った値：{args}')

    if len(args) == 0:
        print('やること無いので暇です')

    elif len(args) == 1:
        args1 = args[0]
        # args1, = args
        if type(args1) != int and type(args1) != str:
            print('難しくて無理です')
        else:
            print(args1 * 2)

    elif len(args) == 2:
        args1,args2 = args
        if type(args1) == type(args2) != int and type(args1) == type(args2) != str:
            print('無茶言わないで！')
        elif type(args1) != type(args2):
            print('できません〜')
        else:
            print(args1 + args2)

    else:
        print('無理です...')





# main
do_anything()
do_anything(10)
do_anything('asdfg')
do_anything([1, 2, 3])
do_anything(10, 20)
8
do_anything(10, 'abc')
do_anything('x', 'yz')
do_anything([1, 2, 3], [4, 5, 6])
do_anything(1, 2, 3)
