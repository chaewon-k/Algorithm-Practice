def make_list(st):
    maxi = -1
    stack = []; result = []
    number = ''
    # 1-1. stack 을 사용하여 각 튜플을 int 리스트로 변환하여 return.
    # 1-2. 각 리스트 중 maximum 값을 저장해서 같이 return. (중복 원소를 제외하기 위해서 visited 리스트 생성할거임)
    for i in range(1, len(st)-1):
        if st[i] == '{':    stack.append(st[i])
        elif st[i] == ',':
            stack.append(number)
            number = ''
        elif st[i] == '}':
            stack.append(number)
            number = ''
            temp = []
            while stack[-1] != '{':
                temp.append(int(stack.pop()))
            result.append(temp[::-1])
            if maxi < max(temp):    maxi = max(temp)
        else:   number+=st[i]
    
    # 2. 각 리스트를 길이 순으로 오름차순.
    for i in range(len(result)-1):
        for j in range(i+1, len(result)):
            if len(result[i]) > len(result[j]):
                result[i], result[j] = result[j], result[i]

    return maxi, result

def solution(s):
    answer = []
    # 1. 문자열을 리스트로 만들기
    maxi, tuple_list = make_list(s)
    
    # 3. 중복 제거를 위해 visited 리스트 생성
    # 비트마스킹 사랑해
    visited = [0] *(maxi+1)
    
    # 4. 중복 제거한 원소들 찾기
    for i in tuple_list:
        for j in i:
            if not visited[j]:
                visited[j] = 1
                answer.append(j)
    return answer

print(solution("{{20,111},{111}}"))