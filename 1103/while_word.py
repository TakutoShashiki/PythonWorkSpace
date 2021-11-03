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

word = []
while True:

    kaku = str(input("単語を入力してください："))

    if kaku == "":
        break

    if kaku == "LIST":
        print("単語リスト:",word)
        continue

    if kaku in word:
        print("すでに登録済みです")
        continue
    else:
        word.append(kaku)
print("終了します")
print('これまでに覚えた単語:',word)