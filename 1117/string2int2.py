# o str2int( ) 関数を定義する
#  文字列を数値（整数）に変換して、値を返す。
#  変換できない場合は 0 を返す
#  文字列でない場合は、そのまま値を返す。
# 【実行結果】
# > python string2int.py
# 0
# 10
# 100

def list2int(s):
    """list2int 
    文字列を数値に変換した値を返す(List対応)
    """

    if type(s) is str:  # 文字列かどうかの確認
        return list2int(s)
    elif type(s) is list:  # 文字列ではなくリストかどうかの条件式
        #result = [str2int(i) for i in s]
        result = []
        for i in s:
            result.append(list2int(i))
        return result
    else:
        return None


print(list2int(['5', 'ab', '100', 10, 1]))
print(list2int('100'))
print(list2int('xyz'))
