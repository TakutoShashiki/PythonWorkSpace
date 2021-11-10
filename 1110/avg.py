# 練習 6
#  上記と同一の test.csv を用いて、次のプログラムを作成してください。【avg.py】
# o test.csv を読み込む
# o 各教科ごとの平均点を求めて出力する
# 2
# 【実行結果】
# > python avg.py
# ['国語', '算数', '理科', '社会']
# [67.5, 77.5, 77.5, 82.5]

import numpy

DATE_FILENAME = 'test.csv'
person_data = []

with open(DATE_FILENAME, 'r', encoding='utf-8') as f:
    title = f.readline().strip().split(',')                 #1行目の読み込み
    for line in f:                                          #残りの行を読み込み
        person_data.append(line.strip().split(','))         #「,」で分割して格納 & 行末の改行を取り除く
print('person_dataは',person_data)

col = 1                                                     #[0]は名前なので skip [1]から
avg = [0] * len(title)                                      #平均を格納するリスト
while col < len(title):
    for score in person_data:                               #全員分の科目得点の処理
        avg[col] += int(score[col])/len(person_data)
    col += 1                                                #次の科目
print(title[1:])                                       
print(avg[1:])