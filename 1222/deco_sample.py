# デコレータ
#  既存の関数の中身を変更せず、機能追加するための方法
# o オブジェクトとして関数を渡す・受け取る
# o 関数内関数
# o * args, **kwargs の利用
#  既存のライブラリなどを利用する場合などに有効


def startend(func):
    def funcname(*args, **kwargs):
        print('[start]--')
        reslut = func(*args, **kwargs)
        print('--[end]')
        return reslut
    return funcname


def test(n):
    print('test->{}'.format(n))


# main
test(10)  # 通常の呼出
# デコレータ使用
deco_func = startend(test)
deco_func(20)
# 同一の関数名でデコレータ使用
test = startend(test)
test(30)
# @記法を使用


@startend
def test2(n):
    print('test2->{}'.format(n))


test2(100)
