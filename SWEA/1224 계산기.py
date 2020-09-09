for t in range(1,11):
    N = int(input())
    formula = input()
    stack = []; postfix = []
    for i in formula:
        if i.isdigit() == True:     #피연산자 (숫자) 경우
            postfix.append(i)
        else:                       #연산자 경우
            if stack:               #stack이 비어있지 않을 경우
                if i == '(':    stack.append(i)
                elif i == ')':
                    while stack[-1] != '(':
                        postfix.append(stack.pop())
                    stack.pop()
                elif i == '+':
                    while len(stack)>=1:
                        if stack[-1] == '*' or stack[-1] == '+':    postfix.append(stack.pop())
                        else:
                            stack.append(i)
                            break
                    if len(stack) == 0: stack.append(i)
                else:   stack.append(i)

            else:
                stack.append(i)     #stack이 비어있을 경우

    while len(stack) != 0:
        postfix.append(stack.pop())

    new_arr = []
    for i in postfix:
        if i.isdigit() == True:
            new_arr.append(int(i))
        else:
            a = new_arr.pop()
            b = new_arr.pop()
            if i == '+':    new_arr.append(a+b)
            else:   new_arr.append(a*b)

    print(f'#{t} {new_arr[0]}')