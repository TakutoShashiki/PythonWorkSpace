# o 数字を入力する→記憶する
#  整数のみとする
# o 記号を入力する→記憶する
#  + , - , * , / の 4 種類のみとする
# o = が入力されたら計算結果を出力する
# o eval( )を上手く使うと簡単に作成可能！【調べること】

# 【実行結果】
# > python list_calc.py
# calc :3
# calc :+
# calc :5
# calc :*
# calc :*
# 入力が正しくありません。
# calc :2
# calc :=
# 入力した計算式：3+5*2
# 計算結果：13

calc = []
kigou = True

while True:
    in_str = input('calc :')
    if in_str == '':
        break
    elif in_str == '=':
        break
    elif kigou == True and in_str.isnumeric():
        calc.append(in_str)
        kigou == False

    elif kigou == False and in_str in ['+','-','*','/']:
        calc.append(in_str)
        kigou == True

    else:
        print('入力が正しくありません。')
        continue
formula = ''.join(calc) # 文字列を結合
print(f'入力した計算式:{formula}\n計算結果:{eval(formula)}')
# eval() イーバル：文字列を式として評価