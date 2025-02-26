import os, sys
from collections import deque
from copy import deepcopy

r_move = [1, 0, -1, 0]
c_move = [0, 1, 0, -1]
def bfs(x : int, y : int, map_list : list, dist_list : list) :

    global n, l, r

    union_list = []
    total_count =  map_list[x][y]
    tmp_queue = deque()
    tmp_queue.append((x, y))
    union_list.append((x, y))
    while tmp_queue :
        tx, ty = tmp_queue.popleft()
        t_count = map_list[tx][ty]

        for i in range(4) :
            itx = tx + r_move[i]
            ity = ty + c_move[i]

            if itx < 0 or itx >= n or ity < 0 or ity >= n :
                continue

            if dist_list[itx][ity] == 0 :
                n_count = map_list[itx][ity]
                diff = abs(t_count - n_count)

                if l <= diff <= r :
                    dist_list[itx][ity] = 1
                    tmp_queue.append((itx, ity))
                    union_list.append((itx, ity))
                    total_count += map_list[itx][ity]

    return union_list, total_count

def main() :

    # with open('input.txt', 'r') as f :
    #     file_list = f.read().splitlines()

    file_list = sys.stdin.read().splitlines()

    global  n, l, r

    n, l, r = map(int, file_list[0].split())

    map_list = []



    for i in range(n) :
        map_list.append(list(map(int, file_list[1 + i].split())))

    move_day = 0

    while True :
        dist_list = [[0] * n for _ in range(n)]
        change_map = deepcopy(map_list)
        b_move = 0

        #union 체크 -> 인구 이동
        for i in range(n) :
            for j in range(n) :
                if dist_list[i][j] == 0 :
                    dist_list[i][j] = 1
                    union_list, total_count = bfs(i, j, change_map, dist_list)

                    if len(union_list) > 1 :
                        b_move = 1
                        average = int(total_count / len(union_list))

                        for x, y in union_list :
                            change_map[x][y] = average

        map_list = change_map
        if b_move == 0 :
            break
        move_day += 1
    print (move_day)
    return

if __name__ == "__main__" :
    main()