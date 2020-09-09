T = int(input())
for t in range(T):
    card = input()
    arr = []
    flag = 0
    number = [0,0,0,0]
    for i in range(0, len(card),3):
        temp = card[i:i+3]
        if temp in arr:
            print(f'#{t+1} ERROR')
            flag = -1
            break
        else:
            arr.append(temp)
            if temp[0] == 'S': number[0] += 1
            elif temp[0] == 'D': number[1] += 1
            elif temp[0] == 'H': number[2] += 1
            else:   number[3] += 1

    if flag != -1:
        print(f'#{t+1} {13-number[0]} {13-number[1]} {13-number[2]} {13-number[3]}')