import os, sys
from collections import deque

'''
   1
   2
5  3  6
   4
'''

# 주사위의 현재 상태 (인덱스: 0 = 윗면, 5 = 바닥면)
nDice = [0, 0, 0, 0, 0, 0]

def roll(dir):
    """주어진 방향으로 주사위를 굴림"""
    a, b, c, d, e, f = nDice  # 현재 주사위 값 복사
    if dir == 1:  # 동쪽 (오른쪽 이동)
        nDice[0], nDice[2], nDice[3], nDice[5] = d, a, f, c
    elif dir == 2:  # 서쪽 (왼쪽 이동)
        nDice[0], nDice[2], nDice[3], nDice[5] = c, f, a, d
    elif dir == 3:  # 북쪽 (위로 이동)
        nDice[0], nDice[1], nDice[4], nDice[5] = e, a, f, b
    elif dir == 4:  # 남쪽 (아래로 이동)
        nDice[0], nDice[1], nDice[4], nDice[5] = b, f, a, e

def main():
    # 파일 입력 (입출력부 수정하지 않음)
    # fileData = open('input.txt', 'r')
    # fData = fileData.read().splitlines()
    fData = sys.stdin.read().splitlines()
    N, M, X, Y, K = map(int, fData[0].split())

    # 지도 입력 (정수 변환)
    sMap = [list(map(int, fData[1 + i].split())) for i in range(N)]

    # 명령어 입력
    sMove = list(map(int, fData[1 + N].split()))

    '''
    마지막 줄에는 이동하는 명령이 순서대로 주어진다.
    동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
    '''
    xM = [0, 0, -1, 1]  # 동, 서, 북, 남 (문제에서 주어진 순서)
    yM = [1, -1, 0, 0]

    # 현재 위치
    tX, tY = X, Y

    for i in range(len(sMove)):
        nIdx = int(sMove[i]) - 1  # 1~4 → 0~3으로 변환

        # 새로운 위치 계산
        tX += xM[nIdx]
        tY += yM[nIdx]

        # 이동 범위 확인 (범위를 벗어나면 무시)
        if tX < 0 or tX >= N or tY < 0 or tY >= M:
            tX -= xM[nIdx]
            tY -= yM[nIdx]
            continue

        # 주사위 굴리기
        roll(nIdx + 1)

        # 지도와 주사위 바닥면 처리
        if sMap[tX][tY] == 0:
            sMap[tX][tY] = nDice[5]  # 주사위 바닥면 값 복사
        else:
            nDice[5] = sMap[tX][tY]  # 지도 값을 주사위 바닥면으로 복사
            sMap[tX][tY] = 0  # 지도 값 초기화

        # 주사위 윗면 출력
        print(nDice[0])

if __name__ == "__main__":
    main()
