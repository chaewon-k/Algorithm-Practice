import re
def removing(id, index):
    if len(id) == 0:
        return 'a'
    else:
        if index == 0 and id[index] == '.':
            return id[1:]
        elif index == -1 and id[index] == '.':
            return id[:-1]
        else:
            return id


def solution(new_id):
    new_id = new_id.lower()

    rem_list = ['.','_','-']
    for i in new_id:
        if i.isdigit() == True or i.isalpha() == True:
            continue
        else:
            if i not in rem_list:
                new_id = new_id.replace(i,'')
    remove_list = ['...', '..']
    for i in remove_list:
        if i in new_id:
            new_id = new_id.replace(i,'.')
    new_id = removing(new_id,0)
    new_id = removing(new_id,-1)
    if len(new_id) == 0:
        new_id = new_id.join('a')
    print(new_id)
    if len(new_id) >= 16:
        new_id = new_id[:14]

    if new_id[-1] == '.':
        new_id = new_id[:-2]

    if len(new_id) <=2:
        temp = new_id[-1]
        while len(new_id)<3:
            new_id += temp
    return new_id

print(solution("z-+.^."))


# def solution(new_id):
#     answer = ''
#     new_id = new_id.lower()
#
#     new_id2 = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', new_id)
#
#     remove_list = ['...', '..']
#     for i in remove_list:
#         if i in new_id2:
#             new_id2 = new_id2.replace(i,'.')
#
#     if new_id2[0] == '.' or new_id2[-1] == '.':
#         if len(new_id2) <= 1:
#             new_id2 = new_id2.replace('.','')
#         else:
#             if new_id2[0] == '.':
#                 new_id2 = new_id2[1:len(new_id2)]
#             else:
#                 new_id2 = new_id2[:len(new_id2)-1]
#
#     if len(new_id2)==0:
#         new_id2 = new_id2.join('a')
#
#     if len(new_id2) > 15:
#         new_id2 = new_id2[:15]
#
#     if new_id2[-1] == '.':
#         new_id2 = new_id2[:len(new_id2)-1]
#
#     if len(new_id2) <=2:
#         temp = new_id2[-1]
#         while len(new_id2)<3:
#             new_id2 += temp
#
#     answer = new_id2
#     return answer




# import itertools
#
# def solution(orders, course):
#     answer = []
#     orders.sort(key=len)
#     for order in range(len(orders)):
#         temp = list(orders[order])
#         temp.sort()
#         word = ''
#         for i in temp:
#             word+=i
#         orders[order] = word
#
#     result_num = []
#     result = []
#
#
#     for n in course:
#         new_arr = []
#         for i in orders:
#             new_arr.append(list(map("".join, itertools.combinations(i,n))))
#
#         li =[]
#         for i in new_arr:
#             for j in i:
#                 if j not in li:
#                     li.append(j)
#         num_list = []
#         for i in li:
#             cnt = 0
#             for j in new_arr:
#                 if i in j:  cnt += 1
#             num_list.append(cnt)
#
#         maxi = max(num_list)
#         if maxi <= 1:
#             break
#         for i in range(len(num_list)):
#             if num_list[i] == maxi and len(num_list) >= 2:
#                 result.append(li[i])
#                 result_num.append(maxi)
#     return sorted(result)
#
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
# import sys
# import heapq
# inpu = sys.stdin.readline
# INF = 999999999
#
# def dijkstra(n, start,end_a,end_b, g):
#     visited = [0 for _ in range(n+1)]
#     distance = [INF for _ in range(n+1)]
#     distance[start] = 0
#     queue = []
#     heapq.heappush(queue, (0, 0))
#     # 큐가 빌대까지 반복
#     while queue:
#         # 큐에서 확인할 노드번호를 꺼냄
#         d, idx = heapq.heappop(queue)
#         if visited[idx]:
#             continue
#         # 방문 체크를 하고
#         visited[idx] = 1
#         # 그 노드와 연결된 노드를 찾는다.
#         for a, b in g[idx]:
#             # a는 노드번호, b는 노드간 거리
#             # 0번부터 노드a까지의 거리가 지금가는 경로보다
#             # 비용이 크다면 갱신
#             if distance[a] > d + b:
#                 distance[a] = d + b
#                 heapq.heappush(queue, (distance[a], a))
#     print(distance)
#     return distance
#
#
# def solution(n, s, a, b, fares):
#     answer = 0
#     adj = [[] for _ in range(n+1)]
#     for t in range(len(fares)):
#         adj[fares[t][0]].append((fares[t][1], fares[t][2]))
#
#     result = dijkstra(n,s,a,b,adj)
#
#     return answer
#
# print(solution(6,4,6,2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24],
#                          [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
