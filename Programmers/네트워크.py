def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]

    def dfs(start):
        print(start)
        stack = [start]

        while stack:
            com_num = stack.pop()
            if visit[com_num] == 0:
                visit[com_num] = 1
            for i in range(len(computers[0])):
                if computers[com_num][i] == 1 and visit[i] == 0:
                    stack.append(i)
    i = 0
    while 0 in visit:
        print(visit)
        if visit[i] == 0:
            dfs(i)
            answer += 1
        i += 1
    return answer

# print(solution(3,[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
# print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(6, [[1,1,0,1,0,0],[1,1,0,0,0,0],[0,0,1,0,0,1],[1,0,0,1,1,0],[0,0,0,1,1,0],[0,0,1,0,0,1]]))