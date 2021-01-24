# def getMinimumMoves(arr):
#     dp = [1]*len(arr)
#     for i in range(len(arr)):
#         for j in range(i):
#            if arr[i] > arr[j]:
#                dp[i] = max(dp[i], dp[j]+1)
#     return max(arr)-max(dp)


def getMinimumMoves(arr):
    index_list = {elem: i for i, elem in enumerate(sorted(arr))}
    result = 0
    for idx, par in enumerate(arr):
        if idx != index_list[par] + result:
            result += 1
    return result

print(getMinimumMoves([5,1,3,2]))