# def solution(n):
#     limit = n*(n+1)//2
#     answer = [0]*limit
#     num_list = [i for i in range(1,limit+1)]
#     turn = 1
#     cnt = n
#     i = num = 0
#     jump = 0
#     while num < limit:
#         if turn%3 == 1:
#             jump += 1
#             temp_cnt = cnt
#             for j in range(temp_cnt, 0,-1):
#                 answer[i] = num+1
#                 i += jump
#                 jump += 1
#                 num+=1
#             i -= jump-2
#
#         elif turn%3 == 2:
#             temp_cnt = cnt
#             for j in range(temp_cnt,0,-1):
#                 answer[i] = num+1
#                 num+=1
#                 i+=1
#             i -= (n+1)
#
#         else:
#             jump = n-1
#             temp_cnt = cnt
#             for j in range(temp_cnt,0,-1):
#                 answer[i] = num+1
#                 num+=1
#                 i -= jump
#                 jump -= 1
#             i += jump + 3
#
#         turn += 1
#         cnt -=1
#         print(answer)
#
#     return answer






from itertools import chain

def solution(n):
    maps = [[0 for _ in range(n)] for _ in range(n)]
    y, x = -1,0
    number = 1
    for i in range(n):
        for j in range(i,n):
            if i%3==0:
                y += 1
            elif i%3 == 1:
                x+=1
            else:
                y-=1; x-=1
            maps[y][x] = number
            number += 1
    answer = [i for i in chain(*maps) if i != 0]
    return answer

print(solution(5))