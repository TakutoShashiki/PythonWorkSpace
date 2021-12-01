def a(b, c):
    '''2 数の和を求める。和を返す'''
    return (b + c)


def add_two_int(first_int, second_int):
    '''2 数の和を求める。和を返す'''
    return (first_int + second_int)


# main（以下実際に入力してください）
x = 10
y = 20
z = a(b=x, c=y)
print(z)
z = add_two_int(first_int=x, second_int=y)
print(z)
