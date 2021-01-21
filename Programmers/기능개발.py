def solution(progresses, speeds):
    answer = []
    day_list = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] >= 1:
            day = (100-progresses[i])//speeds[i]+1
        else:
            day = (100-progresses[i])//speeds[i]
        day_list.append(day)
    day_list.append(0)

    maxi = day_list[0]
    cnt = 1
    for i in range(1, len(day_list)):
        if day_list[i] == 0:
            answer.append(cnt)
            break
        if day_list[i] > maxi:
            answer.append(cnt)
            cnt = 1
            maxi = day_list[i]
        else:
            cnt += 1
    return answer

#### 좋은 예 ####
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]

print(solution([93,30,55],[1,30,5]))
# print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))