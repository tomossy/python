def print_board(players):
    for i in range(9):
        # マスが埋まっているかで振り分け
        if (players[0] & (1 << i)) > 0:
            print("○", end='')
        elif (players[1] & (1 << i)) > 0:
            print("×", end='')
        else:
            print("□", end='')
        if i % 3 == 2:
            print()
    print()

# 勝敗が決まった場合の配置をゴールとして設定
goal = [
    0b111000000, 0b000111000, 0b000000111, 0b100100100,
    0b010010010, 0b001001001, 0b100010001, 0b001010100
]

def check_win(player):
    for mask in goal:
        # マスクとのAND演算の結果をチェック
        if player & mask == mask:
            return True
    return False

def check_end(players):
    # OR演算ですべてのマスが埋まっているか確認
    if (players[0] | players[1]) == 0b111111111:
        return True
    return False

turn = 0  # ○のとき0、×のとき1
players = [0, 0]
user = ["○", "×"]

import random

def play_human(players):
    r = input('行番号(0〜2)：')
    c = input('列番号(0〜2)：')
    pos = int(r) * 3 + int(c)
    if ((players[0] | players[1]) & (1 << pos)) > 0:
        print('この場所は埋まっています')
        return -1
    else:
        return pos

def minmax(p1, p2, turn):
    if check_win(p2):
        if turn:
            return 1
        else:
            return -1
        
    if check_end([p1, p2]):
        return 0
    
    board = p1 | p2
    w = [i for i in range(9) if (board & (1 << i)) == 0]

    if turn:
        return min([minmax(p2, p1 | (1 << i), not turn) for i in w])
    else:
        return max([minmax(p2, p1 | (1 << i), not turn) for i in w])

def play_com(players):
    board = players[0] | players[1]
    w = [i for i in range(9) if (board & (1 << i)) == 0]
    # 人間が○で先手のとき↓
    r = [minmax(players[0], players[1] | (1 << i), True) for i in w]
    i = [i for i, x in enumerate(r) if x == max(r)]
    # ランダムに1つ選ぶ
    return w[random.choice(i)]

turn = 0
players = [0, 0]
user = ["○", "×"]
play = [play_human, play_com]

while True:
    print_board(players)
    pos = play[turn](players)
    if pos >= 0:
        players[turn] |= (1 << pos)
        if check_win(players[turn]):
            print_board(players)
            print(user[turn] + 'の勝ち')
            players = [0, 0]
        elif check_end(players):
            print_board(players)
            print('引き分け')
            players = [0, 0]
        else:
            #手番を入れ替える
             turn = 1 - turn
