import random

maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 9, 0, 9, 9],
    [9, 0, 9, 9, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 9, 9, 9, 9],
    [9, 9, 0, 9, 0, 9, 0, 1, 9],
    [9, 0, 0, 9, 0, 0, 0, 9, 9],
    [9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9]
]

#進行方向をセット
d = [[0, -1], [-1, 0], [0, 1], [1, 0]]

def search(log):
    x, y = log[-1] # 最後の位置を取得
    if maze[x][y] == 1:
        # ゴールしたら深さ（経路の長さ）を返す
        return len(log) - 1
    depth = [99999] # 深さとして十分大きな値をセット
    for move in d:
        if maze[x + move[0]][y + move[1]] != 9:
            if [x + move[0], y + move[1]] not in log:
                # 過去に移動していない場所であれば移動
                log.append([x + move[0], y + move[1]]) # プッシュ
                depth.append(search(log)) # 再帰
                log.pop(-1) # ポップ
    return min(depth)

print(search([[1,1]]))
