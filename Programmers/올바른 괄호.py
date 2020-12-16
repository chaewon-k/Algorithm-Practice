def solution(s):
    stack = []
    for i in s:
        if i == "(":    stack.append(i)
        else:
            if not stack:
                return False
            stack.pop(0)
    if stack:
        return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))