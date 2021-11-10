# 練習 4
#  次のプログラムを作成してください。【linenum.py】
# o 先のプログラムで生成した word.txt を読み込む。
#  word.txt が無い場合は、他のテキストファイルでも OK
# o 各行の先頭に行番号を 4 桁で出力する。
# 【実行例】
# > python linenum.py
# 0001:help
# 0002:test
# 0003:Good

DATE_FILENAME = 'word.txt'

with open(DATE_FILENAME) as f:
    line_num = 1
    for line in f:
        print('{0:04d}:{1}'.format(line_num, line.strip())) # 0001:テキスト

        line_num += 1