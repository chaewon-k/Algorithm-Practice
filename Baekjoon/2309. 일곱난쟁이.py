tall_list = []
for _ in range(9):
    tall_list.append(int(input()))

flag = 0
for i in range(9):
    for j in range(i+1, 9):
        temp = [tall_list[i],tall_list[j]]
        temp_sum = []
        for m in tall_list:
            if m not in temp:
                temp_sum.append(m)
        if sum(temp_sum) == 100:
            flag = -1
            break
    if flag == -1:  break
temp_sum.sort()
for i in temp_sum:
    print(i)