T = int(input())
for t in range(T):
    stack = []
    formula = input().split()
    flag = 0
    for i in range(len(formula)-1):
        if formula[i].isdigit() == True: stack.append(formula[i])
        else:
            try:
                a = int(stack.pop())
                b = int(stack.pop())
                if formula[i] == '+':   stack.append(b+a)
                elif formula[i] == '*': stack.append(b*a)
                elif formula[i] == '-': stack.append(b-a)
                elif formula[i] == '/': stack.append(b//a)
            except:
                flag = -1

    if flag  == -1 or len(stack)>=2:
        print(f'#{t+1} error')
        continue
    print(f'#{t+1} {stack[0]}')