#  以下のプログラムを while を使って作成してください
# o プログラム名【sheep.py】
# o time モジュールの sleep()を使用すると、一定時間ウェイトをかけることができる。
# o 最初にいくつまで数えるか尋ねる
#  最大 100 匹までとする
# o 「羊が 1 匹」「羊が 2 匹」…と指定した値までカウントする
# o 徐々にゆっくりと数えるようにする。

# 【実行結果】
# > python sheep.py
# 何匹数えますか？：10
# 羊が 1 匹
# 羊が 2 匹
# 羊が 3 匹
# 羊が 4 匹
# 羊が 5 匹
# 羊が 6 匹
# 羊が 7 匹
# 羊が 8 匹
# 羊が 9 匹
# 羊が 10 匹

input_num = int(input("何匹数えますか？："))

import time
i = 0
a = 0
while i < 101:
    i += 1
    if a < input_num :
        a += 1
        time.sleep(3)
        print("羊が",a ,"匹")
    else:
        break
else:
    print("おやすみ")    


#別解
import time

while True:
    max_num = int(input("何匹数えますか？："))
    if max_num > 100:
        print("多すぎます")
        continue
    else:
        break

my_count = 1
while my_count <=  max_num:
    print("羊が{}匹".format(my_count))   