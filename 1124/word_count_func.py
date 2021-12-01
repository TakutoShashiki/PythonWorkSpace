#  先の練習では、あらかじめ加工したデータを使用したが、元のデータをそのまま利用して、カ
# ウントできるようにしてみよう。【word_count_func.py】
#  ファイル「sentence.txt」に元の文章を入れたファイルを用意する。
#  いくつか関数を作成もしくは組み込み関数を利用する
# o 大文字→小文字変換
# o 余分な記号を削除
# o 単語に切り分ける
# o などなど
#  作成した関数などを利用して、sentence.txt→小関数→単語リスト→カウント→出力
# o 正規表現が使えると、もっと簡単に作成できるのだが…。
# o 自力で頑張れる人は、正規表現にチャレンジ！

# 【実行結果】
# > python word_count_func.py
# a :1
# about :2
# article :1
# disambiguation:1
# edition :1
# encyclopedia :3
# encyclopedias :2
# english :2

def word_lower(string):
    '''文字列の中の大文字を小文字に変換し、文字列を返す'''
    return string.lower()

def delete_char(string):
    '''NG Listの記号をスペースに置き換え文字列を返す'''
    ng_list = '.,:()"[]'
    for c in ng_list:
        string = string.replace(c,'')
        return string

def word_split(string):
    '''文字列をスペースで切り分け、リストを返す'''
    words = string.split(' ')
    return words

def remove_null(string):
    '''空のkeyの要素を削除する。辞書を返す'''
    words_list = []
    if DATA_FILENAME == '':
        del keys()
    # if
    #     del

    return words_list


DATA_FILENAME = 'sentence.txt'              # 利用ファイルの指定

word_dic = {}                               # 空の辞書を作成
with open(DATA_FILENAME) as f:
    # word_dic = {}                         #ここに書いても良い
    for line in f:
        line = line.strip()                 # 改行コードを取り除く
        line = word_lower(line)
        line = delete_char(line)
        print(line)                         #上記の処理後
        line = word_split(line)

        for word in word:
            if word in word_dic:            # 辞書のキーに単語が存在するか？
            # if word in word_dic.keys():   #別の書き方
                word_dic[word] += 1         # カウントアップ
            else:
                word_dic[word] = 1          # 初めての単語なので初期値１
        word_dic = remove_null(word_dic)

len_max = 0
for word in word_dic.keys():
    len_max = max(len_max, len(word))
