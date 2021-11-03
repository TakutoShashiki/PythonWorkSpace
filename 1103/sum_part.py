#  次のプログラムを作成してください。
# o 2 つの数字を入力し、その 2 数を含む範囲の合計を求める。【sum_part.py】
# 【実行例】
# > python sum_part.py
# 数字 1：3 【<-数字を入力】
# 数字 2：6 【<-数字を入力】
# 3 から 6 までの合計は 18 です

input_num1 = int(input("数字１："))
input_num2 = int(input("数字２："))

my_sum = 0
for i in range(input_num1,input_num2+1):
    my_sum += i
print('{0}から{1}までの合計は{2}です'.format(input_num1,input_num2,my_sum))