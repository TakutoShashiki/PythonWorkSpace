#  仮引数の先頭に「**」をつけることで、キーワード引数を辞書としてまとめることが可能にな
# る。
# https://qiita.com/hikurochan/items/e6db0feb24f754361d4f
#  あらかじめ辞書を作成し、「 **変数 」として渡すこともできる。
# o テキスト P.158 の「引数リストのアンパック」は、充分な理解が必要！
# o 良く読んでください。

#【実行結果】
# hello
# ('Mike', 1)
# {'desert': 'banana', 'drink': 'beer'}
# desert banana
# drink beer
# hi
# ('Nancy', 2)
# {'math': 15, 'science': 100}
# math 15
# science 100

#args と kwargs を併用する場合は、順番に注意
def say_dic(word, *args, **kwargs):
    print(word)
    print(args)
    print(kwargs)
    for k, v in kwargs.items():
        print(k,v)
say_dic('hello', 'Mike',1, desert='banana', drink='beer')
#辞書にしてから渡す方法
t = {'math':15, 'science':100}
say_dic('hi', 'Nancy', 2, **t)
