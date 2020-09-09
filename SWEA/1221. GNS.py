T = int(input())
num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(T):
    t_case, n = map(str, input().split())
    n = int(n)
    array = list(map(str, input().split()))
    result = []
    print(t_case)
    for i in num_list:
        for j in array:
            if i==j:
                print(i, end=' ')