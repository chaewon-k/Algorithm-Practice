def solution(program, flag_rules, commands):
    answer = []
    # 1. flag_rules 를 딕셔너리 형태로 저장한다.
    rules_dict = {}
    for rules in flag_rules:
        rule = rules.split()
        rules_dict[rule[0]] = rule[1]

    # 2. 모든 command들을 검토한다.
    for command in commands:
        # 2-1. 모든 조건을 통과하면 디폴트 값인 True를 answer리스트에 추가한다.
        temp_answer = True
        splited_command = command.split()

        # 2-2. program 이름이 commands의 가장 첫번째에 있는지 확인하고, 없으면 다음 command로 바로 넘어간다.
        if splited_command[0] != program:
            answer.append(False)
            continue

        # 2-3. program이름을 확인한 후, 비교할 while문을 설계한다.
        i = 1
        while i < len(splited_command):
            # 2-3-1. 각 단어를 공백기준으로 분리한다.
            word = splited_command[i]

            ## 2-3-2. 단어가 flag_rules에 존재한다면
            if word in rules_dict.keys():
                ## 2-3-2-1. STRING이라면
                if rules_dict[word] == 'STRING':
                    if i == len(splited_command)-1:     ### 바로 뒤에 문자가 와야하므로, 가장 끝 단어면 안된다.
                        temp_answer = False
                        break
                    else:
                        if splited_command[i+1].isalpha() == False: ### 문자가 아닐 경우
                            temp_answer = False
                            break
                    i += 2

                ## 2-3-2-2. STRINGS라면
                elif rules_dict[word] == 'STRINGS':
                    if i == len(splited_command) - 1:  ### 바로 뒤에 문자가 와야하므로, 가장 끝 단어면 안된다.
                        temp_answer = False
                        break
                    else:
                        num_temp = []
                        for j in range(i + 1, len(splited_command)):
                            if splited_command[j].isalpha() == False:  ### 문자가 아닐 경우
                                break
                            else:
                                num_temp.append(splited_command[j])
                        if len(num_temp) < 1:
                            temp_answer = False

                        i += len(num_temp) + 1

                ## 2-3-2-3. NUMBER라면
                elif rules_dict[word] == 'NUMBER':
                    if i == len(splited_command)-1:     ### 바로 뒤에 숫자가 와야하므로, 가장 끝 단어면 안된다.
                        temp_answer = False
                        break
                    else:
                        if splited_command[i+1].isnumeric() == False:   ### 숫자가 아닐 경우
                            temp_answer = False
                            break
                    i += 2

                ## 2-3-2-4. NUMBERS라면
                elif rules_dict[word] == 'NUMBERS':
                    if i == len(splited_command) - 1:  ### 바로 뒤에 숫자가 와야하므로, 가장 끝 단어면 안된다.
                        temp_answer = False
                        break
                    else:
                        num_temp = []
                        for j in range(i+1, len(splited_command)):
                            if splited_command[j].isnumeric() == False:  ### 숫자가 아닐 경우
                                break
                            else:
                                num_temp.append(splited_command[j])
                        if len(num_temp) < 1:
                            temp_answer = False

                        i += len(num_temp)+1

                ## 2-3-2-5. NULL이라면
                else:
                    if i == len(splited_command)-1:     ### 바로 뒤에 문자가 오지 않아도 된다.
                        break
                    else:
                        if splited_command[i+1] not in rules_dict.keys():   ### rules명령어가 아닐 경우
                            temp_answer = False
                            break
                    i += 1

            ## 2-3-3. 단어가 flag_rules에 존재하지 않는다면
            else:
                temp_answer = False
                break

        answer.append(temp_answer)

    return answer

print(solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))
print(solution("trip", ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]))