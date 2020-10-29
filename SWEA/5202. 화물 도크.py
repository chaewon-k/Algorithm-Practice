T = int(input())
for t in range(1, T+1):
    N = int(input())
    timeline = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        timeline.append(temp)

    timeline.sort(key=lambda time: time[1])
    cnt = 1
    end = timeline.pop(0)[1]
    while len(timeline) != 0:
        next_start, next_end = timeline.pop(0)
        if next_start >= end:
            end = next_end
            cnt += 1

    print(f'#{t} {cnt}')

