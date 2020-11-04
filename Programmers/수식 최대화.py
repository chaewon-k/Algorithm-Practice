from itertools import permutations
import re

def solution(expression):
    answer = 0
    expressions = set(re.findall("\D", expression))     #연산자들 집합 생성 ('\D' : 숫자를 제외한다는 뜻)
    operations = permutations(expressions)              #연산자들 순열 이스트 생성
    temp = re.split('([^0-9])', expression)             #문자열에서 숫자들과 연산자들을 분리
    for operation in operations:                        #operations : [('*', '-'), ('-','*')]
        new_ex = temp[:]   #리스트 복사                   #operation : ('*', '-') / ('-','*')
        for op in operation:                            #op : '*', '-' / '-', '*'
            while op in new_ex:
                op_idx = new_ex.index(op)               #특정 연산자 찾기 (우선순위대로 돌리기위해)
                new_num = str(eval(new_ex[op_idx-1]+new_ex[op_idx]+new_ex[op_idx+1]))   #eval : 문자열을 계산 식으로 바꿔주는 함수
                new_ex[op_idx-1] = new_num      #계산 후 리스트에 넣기
                new_ex.pop(op_idx)              #계산한 숫자들 제거
                new_ex.pop(op_idx)
        if answer < abs(int(new_ex[0])):        #최대값 비교.
            answer = abs(int(new_ex[0]))

    return answer

result = solution("100-200*300-500+20")
print(result)