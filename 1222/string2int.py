# o str2int( ) 関数を定義する
#  文字列を数値（整数）に変換して、値を返す。
#  変換できない場合は 0 を返す
#  文字列でない場合は、そのまま値を返す。
# 【実行結果】
# > python string2int.py
# 0
# 10
# 100

def str2int(s):
    """str2int 文字列を数値に変換した値を返す"""

    if type(s) is str :     #文字列かどうかの確認
        #文字列の時
        if s.isnumeric():   #数値かどうかの確認
            return int (s)  #true
        else:
            return 0        #false
    else:
        return s            #文字列ではなかったとき

print(str2int('a'))
print(str2int('10'))
print(str2int(100))
