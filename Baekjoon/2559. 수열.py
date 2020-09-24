N, K  = map(int, input().split())
arr = list(map(int, input().split()))
temp= sum(arr[:K])
maxi = temp

for i in range(K, N):
    temp -= arr[i-K]
    temp += arr[i]
    if temp > maxi:
        maxi = temp
print('#1 {}' .format(maxi))
