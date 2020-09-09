def Bin(members, i, j):
    if i == j:  return i
    else:
        idx1 = Bin(members, i, (i+j)//2)
        idx2 = Bin(members, (i+j)//2+1, j)
        a = members[idx1-1]
        b = members[idx2-1]
        if a > b:
            if a == 3 and b == 1:   return idx2
            else:   return idx1
        elif a < b:
            if a == 1 and b == 3:   return idx1
            else:   return idx2
        else:   return idx1

T = int(input())
for t in range(T):
    N = int(input())
    members = list(map(int,input().split()))

    result = Bin(members, 1, N)
    print(f'#{t+1} {result}')