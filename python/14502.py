import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

def bfs(virus_map):
    """바이러스가 퍼지는 과정 (BFS)"""
    queue = deque()

    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 2:  # 바이러스 위치 큐에 저장
                queue.append((i, j))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and virus_map[nx][ny] == 0:
                virus_map[nx][ny] = 2  # 바이러스 확산
                queue.append((nx, ny))

    return sum(row.count(0) for row in virus_map)  # 안전 영역 개수 계산

def main():
    global N, M, map_list
    input = sys.stdin.read
    file_list = input().splitlines()

    N, M = map(int, file_list[0].split())
    map_list = [list(map(int, file_list[i + 1].split())) for i in range(N)]

    empty_spaces = [(i, j) for i in range(N) for j in range(M) if map_list[i][j] == 0]
    max_safe_area = 0

    for walls in combinations(empty_spaces, 3):  # 벽 3개를 세우는 모든 조합
        temp_map = deepcopy(map_list)  # 원본 맵을 변경하지 않도록 복사

        for x, y in walls:
            temp_map[x][y] = 1  # 벽 세우기

        safe_area = bfs(temp_map)  # 바이러스 확산 후 안전 영역 계산
        max_safe_area = max(max_safe_area, safe_area)

    print(max_safe_area)

if __name__ == "__main__":
    main()
