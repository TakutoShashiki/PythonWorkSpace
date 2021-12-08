# 【実行結果】
# > python vote.py
# 票の数は 0 です vote_box: []
# 投票します
# 投票します
# 投票します
# 投票します
# 投票します
# 投票します
# 投票します
# 投票します
# 投票します
# 投票します
# 票の数は 10 です vote_box: ['票', '票', '票', '票', '票', '票', '票', '票', 
# '票', '票']
# 箱を空にします
# 投票します
# 投票します
# 票の数は 2 です vote_box: ['票', '票']

#p.168
vote_box = []
label = '票'

def vote():
    print('投票します')
    vote_box.append(label)

def reset_box():
    print('箱を空にする')
    vote_box.clear()

def check_box():
    print('票の数は{}です'.format(len(vote_box)), end = '')
    print('vote_box :',vote_box)

# main
check_box()
for i in range(10):
    vote()

check_box()
reset_box()
vote()
vote()
check_box()