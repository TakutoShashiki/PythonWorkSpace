# 練習 5
#  次のプログラムを作成してください。【total.py】
# o test.csv を読み込む
# o 「,」で区切られているので、分割する
# o 各人の合計点を出力する
#  文字コードは、UTF-8、改行コードは「¥n」とする。
# o EXCEL で作成し、保存すると上記条件と異なるので注意！
#  文字コード：shift_jis（cp932,ms932 など）
#  改行コード：¥r¥n
# o https://docs.python.org/ja/3.8/library/codecs.html#standard-encodings
# 【実行結果】
# > python total.py
# A 310
# B 290
# C 320
# D 300

DATE_FILENAME = 'test.csv'

with open(DATE_FILENAME, 'r', encoding='utf-8') as f:
    person_data = []                                        #1要素1人分のデータを入れるリスト
    title = f.readline()                                    #1行目の読み込み
    for line in f:                                          #残りの行を読み込み
        line = line.strip()                                 #行末の改行を取り除く
        person_data.append(line.split(','))                 #「,」で分割して格納
        # person_data.append(line.strip().split(','))       #まとめて書いてもOK

for data in person_data:                                    #各人のデータを一人分ずつ処理
    name,scores = data[0],data[1:]                          #名前と得点に分ける
    scores = [int(num)for num in scores]                    #文字列を数字に変換
    total = sum(scores)                                     #合計を求める
    print(name,total)                                       #一人分ずつ出力
