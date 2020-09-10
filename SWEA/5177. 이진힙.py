# def push(v):
#     global cnt
#     cnt += 1
#     heap[cnt] = v
#     cur = cnt
#     parent = cur//2
#
#     while parent and heap[parent] > heap[cur]:
#         heap[parent], heap[cur] = heap[cur], heap[parent]
#         cur = parent
#         parent = cur // 2
#
# T = int(input())
# for t in range(T):
#     cnt = 0
#     N = int(input())
#     arr = list(map(int, input().split()))
#     heap = [0]*(N+1)
#     for a in range(N):
#         push(arr[a])
#
#     summ = 0
#     i = N//2
#     while i>=1:
#         summ += heap[i]
#         i //= 2
#     print(f'#{t+1} {summ}')

###################다른예 1###########
def heap(n):
    if n == 1: return
    if arr[n // 2] > arr[n]:
        arr[n // 2], arr[n] = arr[n], arr[n // 2]
        heap(n // 2)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    for i in range(2, N + 1): heap(i)
    result = 0
    while N > 0:
        N //= 2
        result += arr[N]
    print(f'#{t} {result}')

###################다른예 2###########
# import heapq
# T = int(input())
# for t in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     heap = []
#     for i in arr:
#         heapq.heappush(heap, i)
#     summ = 0
#     i = N//2
#     while i>=1:
#         summ += heap[i-1]
#         i //= 2
#     print(f'#{t+1} {summ}')