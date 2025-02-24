import sys
from itertools import combinations

def check_min(home_list: list, chicken_list: list):
    total_count = 0
    for r, c in home_list:
        min_count = float('inf')  # 큰 값으로 초기화
        for x, y in chicken_list:
            min_count = min(min_count, abs(x - r) + abs(y - c))
        total_count += min_count
    return total_count

def main():
    # 입력 받기
    N, M = map(int, sys.stdin.readline().split())
    map_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 집과 치킨집 좌표 저장
    home_list = [(i, j) for i in range(N) for j in range(N) if map_list[i][j] == 1]
    chicken_list = [(i, j) for i in range(N) for j in range(N) if map_list[i][j] == 2]

    # 최소 치킨 거리 찾기
    min_count = float('inf')
    for chicken in combinations(chicken_list, M):
        min_count = min(min_count, check_min(home_list, chicken))

    print(min_count)

if __name__ == "__main__":
    main()
