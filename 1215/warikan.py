#  支払合計金額と参加者人数を入力するものとする。
#  一人当たりの支払額は、支払合計金額を参加者人数で割った金額とする。
#  支払の単位は 100 円とする。100 円未満は切り上げる。
#  支払金額合計を払って残った分は、幹事がもらえることとする。
# o 関数化して、見やすく分かりやすいプログラムを作成しよう。
#  input_int(メッセージ)
#  メッセージを出力し、入力した値を int に変換して返す
#  calc_payment(支払合計金額,参加者人数)
#  1 人当たりの支払額、幹事の支払額を計算する。
#  リストもしくは辞書で返す
#  output_payment(1 人当たりの支払額,幹事の支払額,参加者人数)
#  引数を分かりやすく出力する

# 【実行結果 例 1】
# 支払合計金額を入力してください：10000
# 参加者人数を入力してください：3
# 支払金額：3,400 円 (2 人)
# 幹事金額：3,200 円

# 【実行結果 例 2】
# 支払合計金額を入力してください：10000
# 参加者人数を入力してください：6
# 支払金額：1,700 円 (5 人)
# 幹事金額：1,500 円

# 【warikan.py】
import math


def input_int(massage):
    '''messageを表示 入力値(int)を返す。数値以外は0を返す'''
    value = input(f'{massage}を入力してください:')
    if value.isnumeric():
        value = int(value)
    else:
        value = 0
    return value


def calc_payment(total, num_pepole):
    '''合計金額と人数から合計を計算する。戻り値は、参加者の金額と幹事の金額を[リスト]で返す'''
    pay_people = total / num_pepole
    pay_people = math.ceil(pay_people / 100) * 100
    pay_coordinator = total - pay_people * (num_pepole - 1)
    return[pay_people, pay_coordinator]


def output_payment(pay_pepole, pay_coordinator, num_peple):
    '''参加者の支払い金額、幹事の支払い金額、参加人数を書式化して出力(戻り値なし) '''
    print(f'支払金額:{pay_pepole}円({num_peple -1}人)')
    print(f'幹事金額:{pay_coordinator}円')


# main
total = input_int('支払い合計金額')
num_pepole = input_int('参加人数')
[pay_pepole, pay_coordinator] = calc_payment(total, num_pepole)
output_payment(pay_pepole,pay_coordinator,num_pepole)
