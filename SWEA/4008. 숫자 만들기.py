def make_formula(n, temp_result):
    global mini, maxi
    if n == N:
        if mini > temp_result:  mini = temp_result
        if maxi < temp_result:  maxi = temp_result
        print(mini)
        print(maxi)
        return

    for i in range(4):
        if op_count[i] != 0:
            op_count[i] -= 1
            if i == 0:  update = temp_result + numbers[n]
            elif i == 1:    update = temp_result - numbers[n]
            elif i == 2:    update = temp_result * numbers[n]
            else:   update = int(temp_result / numbers[n])
            make_formula(n+1, update)
            op_count[i] += 1

T = int(input())
for t in range(1, T+1):
    mini = 100000000
    maxi = -100000000
    N = int(input())
    op_count = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    start = numbers[0]
    make_formula(1,start)
    print(f'#{t} {maxi-mini}')