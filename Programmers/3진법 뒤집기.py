def solution(n):
    answer = 0
    three = []
    while True:
        if n<3:
            three.insert(0,n)
            break
        three.insert(0,n%3)
        n //= 3

    for i in range(len(three)):
        answer += three[i]*(3**i)

    return answer

print(solution(125))