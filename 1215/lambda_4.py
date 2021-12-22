# o 以前作成した、Cards のカードを意味するタプルを作成するプログラムを参考にする。
# 06:sample_3.py
# # 初期化
# marks = ('S','H','C','D') # 4 種類のマーク
# cards = [] # デッキ用リスト
# for m in marks:
#  for n in range(1,14):
#  t = (m,n) # タプルでカード生成
#  cards.append(t) # リストに追加
# print('-'*10)
# print(cards)
# print('-'*10)
# # 1 枚選択
# import random # 乱数用モジュール
# r = random.randrange(52) # 0〜51 の乱数生成
# print(f'選んだカードは{cards[r]}です')
# print(f'選んだカードは{random.choice(cards)}です') # 実は 1 行で書ける
# o カードから、5 枚のカードをランダムに選択する。
# o カードを数字の大きい方から並べ、出力する。
#  sort の key に関してはテキスト P.183 を良く理解しよう！

# 【実行結果】
# > python lambda_3.py
# [('C', 13), ('C', 10), ('S', 8), ('S', 6), ('H', 5)]
# 4

# 【lambda_4.py】
import random
# 初期化
marks = ('S','H','C','D')   # 4種類のマーク
#デッキ用リスト
cards = []
for m in marks :
    for n in range(1,14):
        t = (m,n)           # タプルでカード生成
        cards.append(t)

# 5 枚選択
select_cards = random.sample(cards,5)
# 並び替え
select_cards.sort(reverse=True, key=lambda x: x[1])
#仮引数keyに関数を渡している(ラムダ式の)
# 出力
print(select_cards) 