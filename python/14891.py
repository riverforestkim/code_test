import os, sys
from collections import deque

def left_check(idx : int, direct : int) :

    global wheel_list

    if idx < 0 :
        return

    if wheel_list[idx][2] != wheel_list[idx + 1][6]:
        left_check(idx - 1, -direct)
        wheel_list[idx].rotate(direct)

def right_check(idx : int, direct : int) :

    global wheel_list

    if idx > 3 :
        return

    if wheel_list[idx - 1][2] != wheel_list[idx][6]:
        right_check(idx + 1, -direct)
        wheel_list[idx].rotate(direct)


def main():

    #file_list = open('input.txt', 'r').read().splitlines()

    file_list = sys.stdin.read().splitlines()

    global wheel_list, move_list, K

    wheel_list =[deque(list(map(int, file_list[i]))) for i in range(4)]



    K = int(file_list[4])

    move_list = []

    for i in range(K) :
        wheel_num, direction = map(int, file_list[5 + i].split())

        left_check(wheel_num - 2, -direction)
        right_check(wheel_num, -direction)

        wheel_list[wheel_num - 1].rotate(direction)


    answer = 0

    for i in range(4) :
        if wheel_list[i][0] == 1:
            answer += 2 ** i

    print(answer)

    return


if __name__ == "__main__" :
    main()