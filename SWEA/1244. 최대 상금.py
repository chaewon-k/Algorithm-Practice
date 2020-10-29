def dfs(idx, cnt):
    global maxi, visited
    if cnt == 0:
        temp_result = ''.join(arr)
        if maxi < temp_result and temp_result not in visited:
            maxi = temp_result
        return

    for i in range(idx,length):
        for j in range(i+1, length):
            if arr[i] <= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                dfs(i, cnt-1)
                arr[i], arr[j] = arr[j], arr[i]

    if cnt != 0:
        temp_result = ''.join(arr)
        if str_rev_arr == temp_result:
            temp = set(arr)
            if len(temp) == len(arr):
                if cnt % 2 == 1:
                    arr[-1],arr[-2] = arr[-2],arr[-1]
                    visited.append(temp_result)
                    temp_result = ''.join(arr)
                    maxi = temp_result
                    return

T = int(input())
for t in range(1,T+1):
    string, cnt = map(int, input().split())
    arr = list(str(string))
    rev_arr = arr[:]
    rev_arr.sort(reverse=True)
    str_rev_arr = ''.join(rev_arr)
    visited = []
    maxi = ''.join(arr)
    length = len(arr)
    dfs(0, cnt)
    print(f'#{t} {maxi}')



#####최단시간#######
# for tc in range(1, int(input()) + 1):
#     arr, n = input().split()
#     arr = list(arr);
#     len_arr = len(arr)
#     v = [0] * len_arr
#     n = int(n)
#
#     for i in range(len_arr - 1):
#         max_arr = max(arr[i + 1:])
#         if arr[i] < max_arr:
#             for k in range(len_arr - 1, i, -1):
#                 if arr[k] == max_arr:
#                     v[k] = arr[k]
#                     arr[i], arr[k] = arr[k], arr[i]
#                     n -= 1;
#                     break
#         if not n: break
#
#     fin = 0
#     for i in range(len_arr):
#         if arr[i] in arr[i + 1:]: fin = 1
#         if v[i]:
#             for j in range(i + 1, len_arr):
#                 if v[j] == v[i] and arr[j] > arr[i]:
#                     arr[i], arr[j] = arr[j], arr[i]
#
#     if n % 2 and not fin:
#         arr[-1], arr[-2] = arr[-2], arr[-1]
#
#     print(f'#{tc} {"".join(arr)}')