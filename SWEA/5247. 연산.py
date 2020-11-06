from collections import deque

def bfs(N):
    queue = deque()
    queue.append(N)

    while queue:
        temp = queue.popleft()
        if temp == M:   break
        for i in [temp+1, temp-1, temp*2, temp-10]:
            if 0< i <= 1000000 and not visited[i]:
                queue.append(i)
                visited[i] = visited[temp] + 1

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    visited = [0]*1000001
    bfs(N)
    print(f'#{t} {visited[M]}')