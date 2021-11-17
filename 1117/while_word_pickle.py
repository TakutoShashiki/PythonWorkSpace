#  以下のプログラムを、while を使って作成してください【while_word.py】
# o キーボードから単語を入力する
#  空文字（エンターのみ）の入力で終了する
# o 入力された単語がリストになければ追加する。
#  リストに存在する場合は、その旨メッセージを出力する
# o キーワード「LIST」を入力したら、単語のリストを出力する。

# 【実行例】
# > python while_word.py
# 単語を入力してください：hello
# 単語を入力してください：world
# 単語を入力してください：LIST
# 単語リスト： ['hello', 'world']
# 単語を入力してください：hello
# すでに登録済です
# 単語を入力してください：Good
# 単語を入力してください：bye
# 単語を入力してください：
# 終了します
# これまでに覚えた単語： ['hello', 'world', 'Good', 'bye']

import os
import pickle

DATE_FILENAME = 'word.pkl'

if os.path.isfile(DATE_FILENAME):#ファイルがあるかの確認
    #ここからファイルを読み取る
    with open(DATE_FILENAME) as f:#ファイルを「f」として開く
            words_list = pickle.load(f)

else:   #ファイルがない時
    word_list = [] #リストの作成

word_list = []
while True:

    input_word = input("単語を入力してください：")  #input_wordに入力値格納

    if input_word == "":    #入力値が(空)だった場合
        break               #breakで抜ける

    if input_word == "LIST":            #LISTと入力された時の処理
        print("単語リスト:",word_list)   #単語が入っているリストを出力
        continue                        #contineで続ける

    if input_word in word_list:     #入力された値がリストに存在している場合
        print("すでに登録済みです")
        continue                    #contineで続ける
    else:                               #入力された値がリストに存在していない場合
        word_list.append(input_word)    #入力値をリスト(word_list)につなげている
print("終了します")
print('これまでに覚えた単語:',word_list)

#ファイルに単語リストを書き込む
with open(DATE_FILENAME, 'wb') as f: #モード:ｗとは？
    pickle.dump(word_list,f)
