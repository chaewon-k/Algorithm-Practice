T = int(input())
for t in range(T):
    string = input()
    stack = []
    result = 1
    top = -1
    for i in string:
        if i == '(' or i == '{':
            stack.append(i)
            top += 1
        elif i == ')':
            if top == -1:
                result = 0
                break
            if stack[-1] == '(':
                stack.pop(top)
                top -= 1
            else:
                result = 0
                break
        elif i == '}':
            if top == -1:
                result = 0
                break
            if stack[-1] == '{':
                stack.pop(top)
                top -= 1
            else:
                result = 0
                break

    if top != -1:   result = 0
    print(f'#{t+1} {result}')

