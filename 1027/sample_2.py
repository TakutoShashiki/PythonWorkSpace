# 【実行結果】
# 果物をカタカナで入力してください：リンゴ
# リンゴは、知っています！
# 果物をカタカナで入力してください：イチゴ
# イチゴは、知りませんでした。覚えておきます。
# 果物をカタカナで入力してください：イチゴ
# イチゴは、知っています！
# 果物をカタカナで入力してください：パイナップル 
# パイナップルは、知りませんでした。覚えておきます。
# 果物をカタカナで入力してください：
# 知っている果物
# ['バナナ', 'リンゴ', 'オレンジ', 'イチゴ', 'パイナップル']


# 【sample_2.py】
fruits = ['バナナ','リンゴ','オレンジ']
while True:

    mi = str(input("果物をカタカナで入力してください："))

    if mi == "":
        break

    if mi in fruits:
        print(mi + "は、知っています！")
    else:
        fruits.append(mi)
        print(mi + "は、知りませんでした。覚えておきます。")

print('知っている果物')
print(fruits)