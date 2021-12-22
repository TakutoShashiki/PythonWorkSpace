# o 呼び出した関数の情報をファイルに出力する log_file()デコレータを作成する。
# o テスト用の関数を定義し、正しく実行しているかを確認する main 部分は以下の通り
# o ファイルは、「python.log」とし、書式は以下のようにする。
#  日付 日時 呼び出された関数名 位置引数 キーワード引数

# 【実行例：画面】
# test -> 100
# test -> 0
# test -> 1
# test -> 2
# test -> 3
# test -> 4
# 【実行例：python.log】
# 2020-06-10 18: 57: 40.079496 function: test args: (100,) kwargs: {}
# 2020-06-10 18: 57: 40.079570 function: test args: (0,) kwargs: {}
# 2020-06-10 18: 57: 40.079598 function: test args: (1,) kwargs: {}
# 2020-06-10 18: 57: 40.079617 function: test args: (2,) kwargs: {}
# 2020-06-10 18: 57: 40.079635 function: test args: (3,) kwargs: {}
# 2020-06-10 18: 57: 40.079653 function: test args: (4,) kwargs: {}

import datetime


def log_file(func):
    def funcname(*args, **kwargs):
    # ファイルを使用します
        LOG_FILENAME = 'python.log'
        dt_now = datetime.datetime.now()
        # ファイル操作
        with open(LOG_FILENAME, 'a') as f:
            f.write(
                f'{dt_now}function:{func.__name__}args:{args}kwargs:{kwargs}\n')
        result = func(*args, **kwargs)
        return result
    return funcname
#dt_now = datetime.datetime.now()

# main


@log_file
def test(n):
    print('test->{}'.format(n))


# 呼出
test(100)
# 呼出
for i in range(5):
    test(i)
