# o word_list.txt を 読み込む
#  Wikipedia 英語版の最初の段落：https://en.wikipedia.org/wiki/Wikipedia から引
# 用・加工したもの
# o キー：読み込んだ単語、値：出現回数
# o 辞書のキーに読み込んだ単語があれば、値+1
#  なければ、初期値 1 を設定
# o ファイルを最後まで処理したら、結果を表示

# 【実行結果】
# > python word_count.py
# {'from': 1, 'wikipedia': 4, 'the': 3, 'free': 2, 'encyclopedia': 3,
# 'this': 2, 'article': 1, 'is': 1, 'about': 2, 'for': 5, 'english': 2,
# 'edition': 1, 'see': 5, "wikipedia's": 2, 'home': 1, 'page': 2, 'main':
# 1, 'visitor': 1, 'introduction': 1, 'other': 2, 'uses': 1,
# 'disambiguation': 1, 'redirects': 1, 'here': 1, 'a': 1, 'list': 1, 'of':
# 2, 'encyclopedias': 2, 'lists': 1}

DATA_FILENAME = 'word_list.txt'  # 利用ファイルの指定

word_dic = {}  # 空の辞書を作成
with open(DATA_FILENAME) as f:
    # word_dic = {}                     #ここに書いても良い
    for word in f:
        word = word.strip()  # 改行コードを取り除く
        if word in word_dic:  # 辞書のキーに単語が存在するか？
            # if word in word_dic.keys():   #別の書き方
            word_dic[word] += 1  # カウントアップ
        else:
            word_dic[word] = 1  # 初めての単語なので初期値１

print(word_dic)

# 練習４上記のプログラムを修正してください。
# o 結果が見難いので、キーと値を 1 行ずつ出力する
# o アルファベット順に並び替えて出力する

# 【実行結果】
# a :1
# about :2
# article :1

# 最大文字数を調べる
# len_max = 0
# for word in word_dic.keys():keys()
#     len_max = max(len_max, len(word))
# # sort後　並び変え　出力処理
# for word in sorted(word_dic):
#     for word in sorted(word_dic.keys()):
#         print(f'{word:{len_max}}:{max(word_dic[word])}')

for word in sorted(word_dic):
    # for word in sorted(word_dic.keys()):
    print(f'{word:}:{word_dic[word]}')
