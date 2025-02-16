n, m, h = map(int, input().split())
board = [[0] * n for _ in range(h)]

for i in range(m):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1


def check():
    for i in range(n):
        line = i
        for j in range(h):
            if board[j][line] == 1:
                line += 1
            elif line > 0 and board[j][line - 1] == 1:
                line -= 1
        if line != i:
            return False
    return True


def dfs(cnt, x, y):
    global ans

    if check():
        ans = min(ans, cnt)
        return
    if cnt >= 3 or cnt >= ans:
        return

    for i in range(x, n - 1):
        if x == i:
            now = y
        else:
            now = 0
        for j in range(now, h):
            if board[j][i] == 0 and board[j][i + 1] == 0:
                if i > 0 and board[j][i - 1] == 1:
                    continue
                board[j][i] = 1
                dfs(cnt + 1, i, j + 1)
                board[j][i] = 0


ans = 4
dfs(0, 0, 0)
if ans <= 3:
    print(ans)
else:
    print(-1)