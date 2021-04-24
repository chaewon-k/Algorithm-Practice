def solution(m,k):
    answer = ''
    j = 0
    for i in range(len(m)):
        if j == len(k):
            answer += m[i:]
            break
        if m[i] == k[j]:
            j += 1
        else:
            answer += m[i]
    return answer

print(solution("kkaxbycyz", "abc"))
print(solution("acbbcdc", "abc"))
print(solution("aaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbkkkkkkkkkkkkkkkkkkkkpppppppppppppppppppssssssssssssssssssscccccccccccccccccccccccc", "abkc"))