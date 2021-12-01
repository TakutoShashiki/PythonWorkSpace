while True:
    num = int(input("整数を入力してください（終了->0）"))

    if num == 0:
        break

    if  num % 2 == 0 :
        print("偶数です。")
    else :
        print("奇数です。")
