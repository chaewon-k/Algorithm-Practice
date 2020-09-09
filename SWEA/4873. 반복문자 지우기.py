T = int(input())
for t in range(T):
    stack = []
    string = input()
    top = -1
    for i in range(len(string)):
        if top == -1:
            top += 1
            stack.append(string[i])
        else:
            if stack[top] != string[i]:
                stack.append(string[i])
                top += 1
            else:
                stack.pop(top)
                top -= 1
    print(f'#{t+1} {len(stack)}')



