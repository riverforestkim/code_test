from collections import deque

def main():
    N = int(input())  # 보드 크기
    K = int(input())  # 사과 개수

    # f = open('input.txt', 'r')
    # fList = f.read().splitlines()

    sMap = [[0] * N for _ in range(N)]  # 보드 초기화

    for _ in range(K):  # 사과 위치 입력
        tX, tY = map(int, input().split())
        sMap[tX - 1][tY - 1] = 2  # 사과 표시

    L = int(input())  # 방향 변환 횟수
    dictMove = {}

    for _ in range(L):  # 방향 변환 정보 입력
        tM, tD = input().split()
        dictMove[int(tM)] = tD  # 정수 키 사용

    # 방향 이동 (오른쪽, 아래, 왼쪽, 위)
    rM = [1, 0, -1, 0]
    cM = [0, 1, 0, -1]

    nIdx = 0  # 초기 방향: 오른쪽
    nTime = 0  # 경과 시간

    qSnake = deque()
    qSnake.append((0, 0))  # 뱀의 초기 위치
    sMap[0][0] = 1  # 뱀 표시

    x, y = 0, 0  # 머리 위치

    while True:
        # 방향 전환 확인
        if nTime in dictMove:
            if dictMove[nTime] == "L":
                nd = 3 if nIdx == 0 else nIdx - 1
                nIdx = nd
            elif dictMove[nTime] == "D":
                nIdx = (nIdx + 1) % 4

        # 이동
        nextX, nextY = x + rM[nIdx], y + cM[nIdx]

        # 벽 또는 자기 몸과 충돌하면 종료
        if nextX < 0 or nextX >= N or nextY < 0 or nextY >= N or (nextX, nextY) in qSnake:
            break

        # 사과가 없으면 꼬리 제거
        if sMap[nextY][nextX] != 2:
            tHX, tHY = qSnake.popleft()
            sMap[tHY][tHX] = 0

        # 머리 추가
        sMap[nextY][nextX] = 1
        qSnake.append((nextX, nextY))

        x, y = nextX, nextY
        nTime += 1

    print(nTime + 1)

if __name__ == "__main__":
    main()
