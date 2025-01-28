import sys

# 방향 벡터 (우, 하, 좌, 상)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, depth, total):
    global max_value

    # 4칸을 모두 채웠을 때 최대값 갱신
    if depth == 4:
        max_value = max(max_value, total)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 범위를 벗어나지 않고, 방문하지 않았다면 진행
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + sMap[nx][ny])
            visited[nx][ny] = False  # 백트래킹

def check_exception(x, y):
    """ㅗ, ㅜ, ㅓ, ㅏ 모양 체크"""
    global max_value

    # ㅗ 모양 (위쪽 3칸, 아래 1칸)
    if x - 1 >= 0 and y + 2 < M:
        max_value = max(max_value, sMap[x][y] + sMap[x][y + 1] + sMap[x - 1][y + 1] + sMap[x][y + 2])

    # ㅜ 모양 (아래쪽 3칸, 위 1칸)
    if x + 1 < N and y + 2 < M:
        max_value = max(max_value, sMap[x][y] + sMap[x][y + 1] + sMap[x + 1][y + 1] + sMap[x][y + 2])

    # ㅓ 모양 (왼쪽 3칸, 오른쪽 1칸)
    if x + 2 < N and y - 1 >= 0:
        max_value = max(max_value, sMap[x][y] + sMap[x + 1][y] + sMap[x + 1][y - 1] + sMap[x + 2][y])

    # ㅏ 모양 (오른쪽 3칸, 왼쪽 1칸)
    if x + 2 < N and y + 1 < M:
        max_value = max(max_value, sMap[x][y] + sMap[x + 1][y] + sMap[x + 1][y + 1] + sMap[x + 2][y])

def main():
    global N, M, sMap, visited, max_value

    # 입력 받기
    input_data = sys.stdin.read().splitlines()
    N, M = map(int, input_data[0].split())

    # 2차원 배열로 변환 (정수형으로 저장)
    sMap = [list(map(int, input_data[i + 1].split())) for i in range(N)]

    # 방문 체크 배열
    visited = [[False] * M for _ in range(N)]
    max_value = 0

    # 모든 좌표에서 DFS 탐색 시작
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, sMap[i][j])  # DFS 시작
            visited[i][j] = False  # 원상복구

            check_exception(i, j)  # 예외 케이스 체크

    print(max_value)

if __name__ == "__main__":
    main()
