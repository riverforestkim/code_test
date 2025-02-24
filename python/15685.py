import sys

# 이동 방향 (→, ↑, ←, ↓)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def draw_dragon_curve(x, y, d, g, vertex_set):
    curve = [d]  # 0세대 방향 저장

    # g세대까지 진행
    for _ in range(g):
        # 현재까지의 드래곤 커브를 역순으로 탐색하며, 90도 회전 추가
        for i in range(len(curve) - 1, -1, -1):
            curve.append((curve[i] + 1) % 4)

    # 시작점 추가
    vertex_set.add((x, y))

    # 드래곤 커브 그리기
    for direction in curve:
        x += dx[direction]
        y += dy[direction]
        vertex_set.add((x, y))

def count_squares(vertex_set):
    count = 0
    for x, y in vertex_set:
        # (x, y)를 기준으로 우측/아래쪽 점들이 존재하는지 확인
        if (x + 1, y) in vertex_set and (x, y + 1) in vertex_set and (x + 1, y + 1) in vertex_set:
            count += 1
    return count

def main():
    # 입력 파일 읽기
    # with open("input.txt", "r") as f:
    #     file_list = f.read().splitlines()

    file_list = sys.stdin.read().splitlines()

    N = int(file_list[0])  # 드래곤 커브 개수
    vertex_set = set()  # 중복 좌표 방지를 위해 set 사용

    for i in range(N):
        x, y, d, g = map(int, file_list[i + 1].split())
        draw_dragon_curve(x, y, d, g, vertex_set)

    # 정사각형 개수 세기
    answer = count_squares(vertex_set)
    print(answer)

if __name__ == "__main__":
    main()
