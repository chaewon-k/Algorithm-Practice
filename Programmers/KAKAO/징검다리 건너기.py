# O(nlogm) binary search
def solution(stones, k):
    answer = 0
    start = 1
    end = 200000000

    while start <= end:
        mid = (start+end)//2
        temp_stones = stones[:]
        for i in range(len(temp_stones)):
            temp_stones[i] -= mid
        cnt = 0
        flag = 0
        for i in temp_stones:
            if i <= 0:  cnt += 1
            else:   cnt = 0

            if cnt >= k:
                end = mid-1
                flag = 1
                break
        if flag == 0:
            start = mid+1

    return start

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))

####################시간 초과#######################
# flag = 0
#     while True:
#         for i in range(len(stones)):
#             if stones[i] != 0:  stones[i] -= 1
#             else:
#                 temp = stones[i:i+k]
#                 if temp.count(0) == k:
#                     flag = -1
#                     break
#         if flag == -1:  break
#         answer += 1