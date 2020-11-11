n,m=map(int,input().split())
arr=list(map(int,input().split()))
s,e=0,0
cnt=0
sum=0
for s in range(n):

    while sum<m and e<n:#합이 m보다 작고, 끝점이 n보다 작으면
        sum+=arr[e]
        e+=1
    if sum==m: #부분합과 같으면
        cnt+=1
    #합이 m보다 크면
    sum-=arr[s]
print(cnt)


# 10 5
# 1 2 3 4 2 5 3 1 1 2