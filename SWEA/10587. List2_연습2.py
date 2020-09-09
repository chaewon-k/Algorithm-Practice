def sub_list_sum(arr):
    total_sub_list = []
    for i in range(1 << 10):
        sub_list = []
        for j in range(10):
            if i & (1 << j):    sub_list.append(arr[j])
        total_sub_list.append(sub_list)

    for i in total_sub_list:
        if sum(i) == 0 and i != []: return 1
    return 0

T = int(input())
for t in range(T):
    my_list = list(map(int,input().split()))
    print(f'#{t+1} {sub_list_sum(my_list)}')


# #교수님 해답
# T = int(input())
# for t in range(T):
#     arr = list(map(int,input().split()))
#     ans = 0
#     for i in range(1,1<<10): #공집합 제외
#         s = 0 #부분집합의 합
#         for j in range(10):
#             if (i&(1<<j)) != 0: #j번 비트가 0이 아니면
#                 s += arr[j]
#         if s == 0:
#             ans =  1
#             break
#     print(f'#{t+1} {ans}')