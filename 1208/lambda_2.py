# o リスト「my_list」内の要素で、文字列の要素リストを作成する。
# 【実行結果】
# > python lambda_2.py
# [1, 2, 'ab', 'xyz', 5, 6, 7, 'zz']
# ['ab', 'xyz', 'zz']


# 【lambda_2.py】
my_list = [1,2,'ab','xyz',5,6,7,'zz']
#list
# 受け取ったイミテータを基にリストを作成する
#filter
#リストなどから抽出条件を元に抽出する
new_list = list(filter(lambda x : type(x) == str , my_list))
print(my_list)
print(new_list)
