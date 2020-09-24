N = int(input())
num_list = list(map(int, input().split()))
result = [1]
for i in range(1,N):
    result.append(i+1)
    result.insert(i-num_list[i],i+1)
    result.pop(-1)
for i in result:
    print(i, end =' ')
