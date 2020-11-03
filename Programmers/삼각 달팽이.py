def solution(n):
    limit = n*(n+1)//2
    answer = [0]*limit
    num_list = [i for i in range(1,limit+1)]
    turn = 1
    cnt = n
    i = num = 0
    while num < limit:

        if turn%3 == 1:
            jump = 1
            temp_cnt = cnt
            for j in range(temp_cnt, 0,-1):
                answer[i] = num+1
                i += jump
                jump += 1
                num+=1
            cnt -= 1
            turn += 1
            i -= jump-2

        elif turn%3 == 2:
            temp_cnt = cnt
            for j in range(temp_cnt,0,-1):
                answer[i] = num+1
                num+=1
                i+=1
            turn+=1
            i -= (n+1)
            cnt -= 1

        else:
            jump = n-1
            temp_cnt = cnt
            for j in range(temp_cnt,0,-1):
                answer[i] = num+1
                num+=1
                i -= jump
                jump -= 1
            turn += 1
            i += jump+3
            cnt -=1
        print(answer)

    print(answer)




    return answer

solution(5)