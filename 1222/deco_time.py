# o 関数の実行時間を実行後に表示する run_time( )デコレータを作成する。
#  呼び出した関数の実行時間を表示する
# o テスト用の関数を作成し、実行時間を表する main 部を作成する。

# 【実行結果】
# > python deco_time.py
# 実行関数:test 実行時間：3.002683162689209
# 実行関数:test 実行時間：10.008330821990967
# 4

# 【deco_time.py】
import time
'''
関数の実行時間を実行後に表示する run_time()デコレータを作成する。
呼び出した関数の実行時間を表示する
テスト用の関数を作成し、実行時間を表示する main 部を作成する
'''

def run_time(func):
    def funcname(*args, **kwargs):
        starttrim = time.time() #現在時刻を取得
        result = func(*args, **kwargs)
        '''実行関数と実行時間を表示'''
        print(f'実行関数:{func.__name__}実行時間:{time.time() - starttrim}')
        return result
    return funcname


    # main

# 実行時間　[time.time() - starttrim]
@run_time
def test(n):
    for i in range(n):
        time.sleep(i)


test(3)
test(5)
