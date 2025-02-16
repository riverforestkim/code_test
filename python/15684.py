import sys

def check():
    """ 현재 사다리가 조건을 만족하는지 확인하는 함수 """
    for start in range(N):
        idx = start
        for j in range(H):
            if ladder[j][idx]:  # 오른쪽 이동
                idx += 1
            elif idx > 0 and ladder[j][idx - 1]:  # 왼쪽 이동
                idx -= 1
        if idx != start:  # 시작 위치와 다르면 실패
            return False
    return True

def dfs(count, x, y):
    """ 백트래킹을 이용한 최소 가로선 탐색 """
    global answer
    if count >= answer:  # 이미 현재 정답보다 많은 경우 중단
        return
    if check():  # 현재 사다리가 올바르면 정답 갱신
        answer = count
        return
    if count == 3:  # 최대 3개까지만 추가 가능
        return

    for i in range(x, H):
        for j in range(N - 1):
            if i == x and j < y:  # 같은 행에서는 이전 열 이후만 탐색
                continue
            if not ladder[i][j] and not ladder[i][j + 1]:  # 가로선 추가 가능
                ladder[i][j] = True
                dfs(count + 1, i, j + 2)  # 연속된 가로선 방지 위해 j+2
                ladder[i][j] = False  # 원상 복구
            if answer != 4:  # 정답 찾았으면 더 탐색할 필요 없음 (가지치기)
                return

def main():
    global N, M, H, ladder, answer

    # 입력 받기
    N, M, H = map(int, sys.stdin.readline().split())
    ladder = [[False] * N for _ in range(H)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        ladder[a - 1][b - 1] = True  # 1-based index 조정

    answer = 4
    dfs(0, 0, 0)  # 백트래킹 탐색

    print(answer if answer < 4 else -1)

if __name__ == "__main__":
    main()
