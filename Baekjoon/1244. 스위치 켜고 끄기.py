N = int(input())
switch = [0]+list(map(int, input().split()))
M = int(input())
for i in range(M):
    s,idx = map(int, input().split())

    if s == 1:      #남학생
        k = idx
        while idx <= N:
            switch[idx] += 1
            idx += k
    else:           #여학생
        jump = 1
        switch[idx] += 1
        while (idx-jump) >= 1 and (idx+jump) <= N:
            if switch[idx-jump] == switch[idx+jump]:
                switch[idx - jump] += 1
                switch[idx + jump] += 1
            else:
                break
            jump += 1
    for j in range(len(switch)):
        temp = switch[j]
        if temp >0:
            switch[j] = temp % 2

switch.pop(0)
cnt = 0
for i in range(N):
    if cnt != 0 and cnt % 20 == 0:
        print()
    print(switch[i], end = ' ')
    cnt += 1




