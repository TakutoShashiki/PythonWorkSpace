# o 1 日の食事を記録する前処理プログラム。カンマ区切りで出力する。
# o 朝食（B)、昼食（L)、夕食（D）の記号と、メニューを入力する
#  区切りは自分で決めて OK
#  順序は問わない
# o 空の入力で、入力処理を終える
# o 食べてない食事は「-」を出力するものとする。

# 【実行結果 1】
# 朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：L,カレー
# 朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：D,ステーキ
# 朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：B,トースト
# 朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：
# ['トースト', 'カレー', 'ステーキ']
# 【実行結果 2】
# 朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：B,小倉トースト
# 朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：D,中華飯
# 朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：
# ['小倉トースト', '-', '中華飯']

# 【func_any.py】
def out_csvdata(**kwargs):
    out_list = []
    for token in kwargs.keys():
        if token in kwargs.keys():
            out_list.append(kwargs[token])
        else:
            out_list.append('-')


# main
eat = {}
while True:
    menu = input("朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：")
    if menu == '':
        break
    token, menu = menu.split(',')
    if token in ['B', 'L', 'D']:
        eat[token] = menu
    else:
        print('記号が間違っています。登録しません')
        continue
out_csvdata(**eat)
