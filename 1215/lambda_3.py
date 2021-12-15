# o リスト「my_list」内の要素の、文字数を数え、5 文字以上の要素のみのリストを作成す
# る。
# 【実行結果】
# > python lambda_3.py
# ['hello', 'nice', 'abc', 'test', 'morning', 'good', 'yes', 'world']
# ['hello', 'morning', 'world']
# 3

# 【lambda_3.py】
my_list = ['hello','nice','abc','test','morning','good','yes','world']
'''5文字以上のリストを作成する'''
new_list = list(filter(lambda x: len(5) >=  my_list))
# p.179

'''
list    リストを作成
map     リストを作成する際、関数を適用
filter  リストを作成する際、条件で抽出
'''

print(my_list)
print(new_list)
