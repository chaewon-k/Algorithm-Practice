T = int(input())

for t in range(T):
    N = int(input())
    my_list = list(map(int, input().split()))

    maxi = my_list[0]
    mini = my_list[0]

    for i in range(1,N):
        if maxi < my_list[i]:
            maxi = my_list[i]
        
        if mini > my_list[i]:
            mini = my_list[i]
    
    print(f'#{t+1} {maxi-mini}')
