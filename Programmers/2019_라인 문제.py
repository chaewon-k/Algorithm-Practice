def find(c,b):
    queue1 = [b]
    i = 1
    while c <= 200000:
        c += i
        i += 1
        queue2 = []
        while queue1:
            num = queue1.pop(0)
            temp1, temp2, temp3 = num - 1, num + 1, 2 * num
            if temp1 == C or temp2 == C or temp3 == C:
                return i
            else:
                if 0 <= temp1 <= 200000:    queue2.append(temp1)
                if 0 <= temp2 <= 200000:    queue2.append(temp2)
                if 0 <= temp3 <= 200000:    queue2.append(temp3)

        queue1 = queue2[:]
    return -1

C, B = map(int, input().split())
print(find(C, B))