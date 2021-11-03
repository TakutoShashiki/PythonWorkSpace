#  次のプログラムを作成してください。
# o 1 以上 99 以下の偶数の一覧を出力する【even.py】
# o 結果は例のように横並びで出力する
# 【実行例 1】
# > python even.py
# 偶数一覧
# =>2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
# 52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,

#解答例1
print('偶数一覧=>',end='')
for i in range(1, 100):
    if i % 2 == 0:
        print(i,end=',')
print()

#解答例2
result = []
for i in range(1, 100):
    if i % 2 == 0:
        result.append(i)
print(f'偶数一覧=>{result}')