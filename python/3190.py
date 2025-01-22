import os
import sys
from collections import deque


def main() :

    # f = open('input.txt', 'r')
    # fList = f.read().splitlines()

    fList = sys.stdin.read().splitlines()

    N = fList[0]
    K = fList[1]

    qApple = deque()
    qMove = deque()
    for i in range(K) :
        tX, tY = map(int, fList[i + 2].split())
        qApple.append([tX, tY])

    L = fList[2 + K]

    dictMove = {}

    for i in range(L) :
        tM, tD = map(str, fList[3 + K + i].split())
        dictMove[tM] = tD

    rM = [1, -1, 0,  0]
    cM = [0, 0, 1, -1]

    nIdx = 0
    nTime = 0
    '''
    게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

    뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
    
    먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

    '''

    qSnake = deque()

    qSnake.append([0, 0])

    while True :

        tHX, tHY = qSnake.popleft()

        nTime += 1

        #Todo
        if dictMove[str(nTime)] == "L" :
            nIdx = nIdx - 1
        elif dictMove[str(nTime)] == "D" :
            #0 -> 3 -> 1 -> 2
            nIdx = nIdx - 3

        #움직임
        tHX += rM[nIdx]
        tHY += cM[nIdx]

        if 0 > tHX or tHX >= N or 0 > tHY or tHY >= N :
            print(nTime)
            break





    return


if __name__ == "__main__" :
    main()