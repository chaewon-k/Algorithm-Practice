def solution(w,h):
    def gcd(a,b):
        if a%b == 0:
            return b
        return gcd(b, a%b)
    answer = w*h - (w+h - gcd(w,h))
    return answer

print(solution(8,12))