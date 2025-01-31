import os, sys


def main():
    # file_list = open('input.txt', 'r').read().splitlines()
    file_list = sys.stdin.read().splitlines()

    N, M = map(int, file_list[0].split())

    # 0 북 1 동 2 남 3 서

    R, C, D = map(int, file_list[1].split())

    move_row = [-1, 0, 1, 0]
    move_col = [0, 1, 0, -1]

    map_list = [list(map(int, file_list[2 + i].split())) for i in range(N)]

    clean_cnt = 0

    # TODO : 방향체크 필요, 방향 플래그를 추가한 뒤, 해당 플래그 값에 따라 변경되는 무브 리스트 추가 필요

    while True:

        # 1. 현재 칸 청소
        if map_list[R][C] == 0:
            map_list[R][C] = 2
            clean_cnt += 1

        clean_flag = 0

        for i in range(4):
            tR, tC = R + move_row[i], C + move_col[i]

            if 0 <= tR < N and 0 <= tC < M and map_list[tR][tC] == 0:
                clean_flag = 1

        # 2. 주변 상하좌우 서치, 청소되지 않은 빈 칸이 없는 경우(0)
        if clean_flag == 0:

            # 0 북 1 동 2 남 3 서
            if D == 0:
                tR, tC = R + move_row[2], C + move_col[2]
            elif D == 1:
                tR, tC = R + move_row[3], C + move_col[3]
            elif D == 2:
                tR, tC = R + move_row[0], C + move_col[0]
            elif D == 3:
                tR, tC = R + move_row[1], C + move_col[1]

            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if map_list[tR][tC] != 1:
                R, C = tR, tC
                continue
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        else:
            # 반시계 90 도 회전
            # 0 북 1 동 2 남 3 서
            if D == 0:
                D = 3
            elif D == 1:
                D = 0
            elif D == 2:
                D = 1
            elif D == 3:
                D = 2
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 칸인 경우 전진
            if D == 0:
                tR, tC = R + move_row[0], C + move_col[0]
            elif D == 1:
                tR, tC = R + move_row[1], C + move_col[1]
            elif D == 2:
                tR, tC = R + move_row[2], C + move_col[2]
            elif D == 3:
                tR, tC = R + move_row[3], C + move_col[3]

            if map_list[tR][tC] == 0:
                R, C = tR, tC

            # 1번 리턴
            continue

    print(clean_cnt)


if __name__ == "__main__":
    main()