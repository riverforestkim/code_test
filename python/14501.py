import sys

def dfs(dT: int, dP: int):
    """DFS를 이용한 완전 탐색"""
    global nMax, N, lst_tp

    # 종료 조건 (퇴사일에 정확히 도달했을 때)
    if dT == N:
        nMax = max(nMax, dP)
        return
    elif dT > N:
        return  # 퇴사일을 넘으면 무효

    # 현재 상담을 선택하는 경우
    if dT + lst_tp[dT][0] <= N:  # 퇴사 전에 끝나는 경우만 선택 가능
        dfs(dT + lst_tp[dT][0], dP + lst_tp[dT][1])

    # 현재 상담을 선택하지 않고 다음 날로 이동하는 경우
    dfs(dT + 1, dP)

def main():
    """입력 처리 및 실행"""
    global nMax, N, lst_tp

    # with open('input.txt', 'r') as f:
    #     file_data = f.read().splitlines()
    file_data = sys.stdin.read().splitlines()
    N = int(file_data[0])
    lst_tp = [list(map(int, file_data[i + 1].split())) for i in range(N)]  # 문자열 -> 정수 변환
    nMax = 0

    dfs(0, 0)

    print(nMax)

if __name__ == "__main__":
    main()
