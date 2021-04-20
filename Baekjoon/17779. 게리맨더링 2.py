N = int(input())
my_map = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

result = float('inf')
# print(result)
for y in range(2, N):
    for x in range(1, N-1):
        for d2 in range(1, N - y + 1):
            for d1 in range(1, min(N-(x+d2) + 1, y)):
                Zone = [0] * 5
                # 1번 구역
                for r in range(1, y):
                    for c in range(1, x + d1 + 1):
                        if r + c < y + x:
                            Zone[0] += my_map[r][c]

                # 2번 구역
                for r in range(1, y - d1 + d2 + 1):
                    for c in range(x + d1 + 1, N + 1):
                        if r - c < y - x - d1 * 2:
                            Zone[1] += my_map[r][c]

                # 3번 구역
                for r in range(y, N + 1):
                    for c in range(1, x + d2):
                        if r - c > y - x:
                            Zone[2] += my_map[r][c]

                # 4번 구역
                for r in range(y - d1 + d2 + 1, N + 1):
                    for c in range(x + d2, N + 1):
                        if r + c > y + x + d2 * 2:
                            Zone[3] += my_map[r][c]

                # 5번 구역
                for r in range(1, 1 + N):
                    for c in range(1, 1 + N):
                        if y + x <= r + c <= y + x + d2 * 2:
                            if y - x - d1 * 2 <= r - c <= y - x:
                                Zone[4] += my_map[r][c]

                sub_res = max(Zone) - min(Zone)
                if sub_res < result:
                    result = sub_res

print(result)