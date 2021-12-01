# o ２つのリストを受け取り、受け取ったリストを結合して返す関数 combine_list( )を作成す
# る。
# o 動作検証用の main 部分を作成し、正常に動作するのを確認してください。
# o なお、リスト以外が渡された場合は、エラー出力し、受け取った引数をリストにして返すものとする。

# 【実行結果】
# > python func_1.py
# [1, 2, 3, 4, 5, 6]
# [4, 5, 6, 1, 2, 3]
# 引数がリストではありません
# ['a', [1, 2, 3]]
# 引数がリストではありません
# [[1, 2, 3], 'xyz']
# 引数がリストではありません
# [10, 'abc']

def combine_list(list1, list2):
    '''2 つのリストを結合し、リストで返す'''
    if type(list1) is list and type(list2) is list:
        # return list1 + list2
        list3 = []
        for i in list1: #a,b,c
            list3.append(i)
        for i in list2: #d,e,f
            list3.append(i)
        return ;list3 #[a,b,c,d,e,f]
    else:
        print('引数がリストではありません')
        return[list1,list2]

# main
# 正常な引数
print(combine_list([1, 2, 3], [4, 5, 6]))
print(combine_list(list2=[1, 2, 3], list1=[4, 5, 6]))
# 誤った引数
print(combine_list('a', [1, 2, 3]))
print(combine_list([1, 2, 3], 'xyz'))
print(combine_list(10, 'abc'))
