# 練習 1
# 【実行結果】
# > python3 list3.py
# a[0, 1, 2, 3, 4, 5]
# d[0, 'a', 'b', 2, 3, 4, 5]
# d[0, 'a', 'b', 2, 'x', 'y', 'z', 4, 5]

# 【list3.py】
a=[0,1,2,3,4,5]
b=['a','b']
c=['x','y','z']
print(a)
d= a[:]                      # a のコピーを作成
d[1:2]= b
print(d)
d[4:5]= c
print(d)



# 練習 2
# 【実行結果】
# python3 list4.py
# 整数を入力してください：5
# 1〜5 までの合計：15
# 平均：3.0

# 【list4.py】
#  リストや sum()、range()、len()などの組み込み関数も使用して作成してください。
#  もちろん、これまでに習ったものはすべて利用して OK
n=input("整数を入力してください")
