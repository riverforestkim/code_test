import os, sys

def check(line:list) :

    global N, L, dist
    for i in range(1, N) :
        if abs(line[i] - line[i - 1]) > 1 :
            return False
        if line[i] < line[i - 1] :
            for j in range(L) :
                if i + j >= N or dist[i+j] or line[i] != line[i + j] :
                    return False
                if line[i] == line[i + j] :
                    dist[i + j] = 1
        elif line[i] > line[i - 1] :
            for j in range(L):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or dist[i - j - 1] :
                    return False
                if line[i - 1] != line[i - j - 1] :
                    line[i - j - 1] = 1
    return True

def main() :

    #file_list = open('input.txt', 'r').read().splitlines()

    file_list = sys.stdin.read().splitlines()

    global N, map_list, dist, L

    N, L = map(int, file_list[0].split())

    map_list = [list(map(int, file_list[i].split())) for i in range(1, N + 1)]

    answer = 0

    for i in range(N) :
        dist = [0 for _ in range(N)]
        if check(map_list[i]) :
            answer +=1

    for i in range(N) :
        dist = [0 for _ in range(N)]
        if check([map_list[j][i] for j in range(N)]) :
            answer +=1

    print(answer)
    return


if __name__ == "__main__" :

    main()