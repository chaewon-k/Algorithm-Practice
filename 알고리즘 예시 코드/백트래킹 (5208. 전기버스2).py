def sol(idx, c):  # idx은 현재 정류장 번호, c는 몇번 충전했는지
    # 현재 정류장 번호에서, 그 정류장에서 갈 수 있는 최대 거리를 더한 것이
    # 마지막 정류장의 번호보다 크면
    if idx + arr[idx] >= N - 1:
        # 몇 번 충전했는 지를 반환한다.
        return c
    # 그렇지 않으면
    else:
        # 지금 갈 수 있는 정류장 번호 중에서
        # 가장 멀리까지 갈 수 있는 거리와 그 때 정류장 번호 저장을 위한 변수 초기화
        maxV = nidx = 0
        # 지금 갈 수 있는 정류장 번호를 순회하면서
        for i in range(idx + 1, idx + arr[idx] + 1):
            # 최대한 멀리 갈 수 있는 정류장을 찾고
            temp = i + arr[i]
            if temp > maxV:
                maxV = temp
                nidx = i
        # 그 정류장을 다음 번 탐색 대상으로 하고 충전 횟수 + 1
        return sol(nidx, c + 1)


for t in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    print(f'#{t} {sol(0, 0)}')