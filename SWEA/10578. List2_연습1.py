T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for t in range(T):
    sol = 0
    N = int(input())
    my_list = []
    for i in range(N):
        my_list.append(list(map(int,input().split())))
    
    for i in range(N):
        for j in range(N):
            for k in range(4):
                temp_i = i + dx[k]
                temp_j = j + dy[k]

                if 0 <= temp_i < N and 0 <= temp_j < N:
                    sol += abs(my_list[i][j] - my_list[temp_i][temp_j])
    print(f'#{t+1} {sol}')
