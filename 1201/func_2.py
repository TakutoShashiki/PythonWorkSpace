# o 金額と消費税から、税込金額を計算する関数 tax_included( )を作成する。
# o 消費税はデフォルト引数として 10%を設定する
# o main 部分も作成してください。

# 【実行結果】
# > python func_2.py
# 5000 の税込金額は 5500 円
# 5000 の消費税 8%の税込金額は 5400 円
# 5000 の消費税-5%の税込金額は None 円

def tax_included(price, tax=10):
    '''税込み金額を計算する。税率を省略した場合は10％になる'''
    if tax < 0:
        return None

    else:
        return int(price * (1+tax/100))

# main
# 5000の税込金額は5500円
print('{}税込金額は{}円'.format(5000,tax_included(5000)))
# 5000 の消費税 8%の税込金額は 5400 円
print('{}税込金額は{}円'.format(5000,tax_included(5000,8)))
# 5000 の消費税-5%の税込金額は None 円
print('{}税込金額は{}円'.format(5000,tax_included(5000,-5)))
