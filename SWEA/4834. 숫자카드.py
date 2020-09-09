T = int(input())

for t in range(T):
    N = int(input())
    a = int(input())
    arr = []
    num_list = [0]*10

    for i in range(N):
        arr.append(a%10)
        a = a//10
    arr.reverse()

    for j in arr:
        num_list[j] += 1

    maximum = -1
    idx = -1

    for i in range(10):
        if maximum <= num_list[i]:
            maximum = num_list[i]
            idx = i

    print(f'#{t+1} {idx} {maximum}')