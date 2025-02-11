import sys
from copy import deepcopy

# CCTV 방향에 따른 이동 (상, 우, 하, 좌)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 주어진 방향으로 맵을 업데이트하는 함수
def draw_map(row, col, direction, sensor_type, temp_map):
    global N, M

    # 특정 방향에 대해 감시 영역 설정
    def fill(row, col, d):
        while True:
            row += DIRECTIONS[d][0]
            col += DIRECTIONS[d][1]
            if row < 0 or row >= N or col < 0 or col >= M or temp_map[row][col] == 6:
                break
            if temp_map[row][col] == 0:
                temp_map[row][col] = "#"

    # CCTV 유형별로 감시 영역 설정
    if sensor_type == 1:
        fill(row, col, direction)
    elif sensor_type == 2:
        fill(row, col, direction)
        fill(row, col, (direction + 2) % 4)  # 반대 방향
    elif sensor_type == 3:
        fill(row, col, direction)
        fill(row, col, (direction + 1) % 4)  # 직각 방향
    elif sensor_type == 4:
        fill(row, col, direction)
        fill(row, col, (direction + 1) % 4)
        fill(row, col, (direction + 2) % 4)  # 반대 방향
    elif sensor_type == 5:
        for i in range(4):  # 모든 방향
            fill(row, col, i)

# DFS로 모든 CCTV 배치를 탐색
def dfs(idx, temp_map):
    global answer

    if idx == len(cctvs):  # 모든 CCTV를 처리한 경우
        uncovered = sum(row.count(0) for row in temp_map)
        answer = min(answer, uncovered)  # 최소 사각지대 갱신
        return

    # 현재 CCTV 정보
    row, col, cctv_type = cctvs[idx]
    for direction in range(4):  # 4방향 탐색
        new_map = deepcopy(temp_map)
        draw_map(row, col, direction, cctv_type, new_map)
        dfs(idx + 1, new_map)

# 메인 함수
def main():
    global N, M, cctvs, answer

    # 입력 처리
    input = sys.stdin.read
    data = input().splitlines()
    N, M = map(int, data[0].split())
    grid = [list(map(int, data[i + 1].split())) for i in range(N)]

    # CCTV 정보 수집
    cctvs = []
    for i in range(N):
        for j in range(M):
            if 1 <= grid[i][j] <= 5:  # CCTV는 1~5
                cctvs.append((i, j, grid[i][j]))

    # 최소 사각지대를 초기화
    answer = float('inf')

    # DFS 실행
    dfs(0, grid)

    # 결과 출력
    print(answer)

if __name__ == "__main__":
    main()
