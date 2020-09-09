T = int(input())
 
for t in range(T):
     
    K, N, M = map(int, input().split())
    bus_stop = [0]*(N+1)
    rev = list(map(int, input().split()))
 
    for i in range(M):
        bus_stop[rev[i]] = 1
     
    ################main#####################
 
    s = cnt = 0
    e = K
 
    while(1):
        distance = 0
 
        for i in range(s+1, e+1):
            if bus_stop[i] == 1: #충전기 스팟에 도착했을 때
                s = i  #시작점으로 지정
            else: #충전기 스팟에 도착하지 않았을 때
                distance += 1 #거리 += 1
 
        if distance == K: #K만큼의 거리가 남았을 때, 종점까지 갈 수 없으므로 종료
            cnt = 0
            break
 
        cnt += 1 
        e = s + K
 
        if e >= N:
            break
         
    print(f'#{t+1} {cnt}')