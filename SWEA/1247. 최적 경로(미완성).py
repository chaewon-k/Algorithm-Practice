def dfs(office,cnt):
    global result
    if cnt > result:    return
    if 0 not in visited:
        cnt += abs(office[0] - home[0]) + abs(office[1] - home[1])
        if result > cnt:
            result = cnt
        return

    for i in range(N):
        temp_x = check[i][0]
        temp_y = check[i][1]
        if not visited[i]:
            visited[i] = 1
            temp = abs(office[0]-temp_x) + abs(office[1]-temp_y)
            dfs([temp_x, temp_y],cnt+temp)
            visited[i] = 0

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    site = list(map(int, input().split()))
    office = [site[0], site[1]]
    home = [site[2], site[3]]
    check = []

    for i in range(2, N+2):
        check.append([site[i*2],site[i*2+1]])

    visited = [0]*N
    result = 100000000
    dfs(office, 0)
    print('#%d %d'%(tc, result))


#### 실행시간 빠른 코드 ########
# def sol(n, k, s):
#     global minV
#     if n == k:
#         s += abs(hx - customer[2 * O[N - 1]]) + abs(hy - customer[2 * O[N - 1] + 1])
#         if s < minV:
#             minV = s
#     else:
#         for i in range(n, k):
#             O[n], O[i] = O[i], O[n]
#             if n == 0:
#                 temp = abs(cx - customer[2 * O[0]]) + abs(cy - customer[2 * O[n] + 1])
#                 if temp < minV:
#                     sol(n + 1, k, temp)
#             else:
#                 temp = s + abs(customer[2 * O[n]] - customer[2 * O[n - 1]]) + abs(
#                     customer[2 * O[n] + 1] - customer[2 * O[n - 1] + 1])
#                 if temp < minV:
#                     sol(n + 1, k, temp)
#             O[n], O[i] = O[i], O[n]
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     t = list(map(int, input().split()))
#     cx, cy, hx, hy = t[0], t[1], t[2], t[3]
#     customer = t[4:]
#     O = list(range(N))
#     minV = 10e5
#     sol(0, N, 0)
#     print(f'#{tc} {minV}')