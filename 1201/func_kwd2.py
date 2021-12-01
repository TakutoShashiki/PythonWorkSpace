# o 商品名と金額を登録するための、チェックプログラムを作成する
# o 金額は 100 円未満の場合エラー表示。すべて 100 円以上なら問題なし。
# o 商品数は何点あるか分からない。

# 【実行結果 1】
# > python func_kwd2.py
# 商品名を入力してください（0:終了）：abc
# 金額を入力してください（0:終了）：100
# 商品名を入力してください（0:終了）：zzzz
# 金額を入力してください（0:終了）：150
# 商品名を入力してください（0:終了）：0
# 全てのデータは問題ありませんでした
# abc : 100
# zzzz : 150

# 【実行結果 2】
# > python func_kwd2.py
# 商品名を入力してください（0:終了）：aaaaa
# 金額を入力してください（0:終了）：80
# 商品名を入力してください（0:終了）：bbbb
# 金額を入力してください（0:終了）：150
# 商品名を入力してください（0:終了）：ccccc
# 金額を入力してください（0:終了）：110
# 商品名を入力してください（0:終了）：ddd
# 金額を入力してください（0:終了）：200
# 商品名を入力してください（0:終了）：0
# 最低価格を下回った商品があります。
# 10
# aaaaa : 80
# bbbb : 150
# ccccc : 110
# ddd : 200

def check_shopping(**kwargs):
    min_price = min(kwargs.values())
    if min_price < 100:
        return False
    else:
        return True


    # main
dic_order = {}

while True:
    product_name = input('商品名を入力してください（0:終了）：')
    if product_name == '0':
        break
    product_price = input('金額を入力してください（0:終了）：')
    if product_price == '0':
        break
    elif product_price.isnumeric():
        product_price = int(product_price)
    else:
        print("数値以外が入力されました")
        continue

    dic_order[product_name] = product_price


if check_shopping(**dic_order):
    print('¥n 全てのデータは問題ありませんでした')
else:
    print('¥n 最低価格を下回った商品があります。')
for key, value in dic_order.items():
    print(f'{key} : {value}')
