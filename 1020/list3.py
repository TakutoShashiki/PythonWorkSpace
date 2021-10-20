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
