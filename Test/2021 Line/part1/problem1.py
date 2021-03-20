def solution(table, languages, preference):
    dict = {}
    for i in range(len(languages)):
        dict[languages[i]] = preference[i]
    answer = ''
    new_table = []
    maxi = -1
    for i in table:
        temp = i.split()
        summ = 0
        for j in range(1, len(temp)):
            if temp[j] in dict.keys():
                summ += (6-j) * dict[temp[j]]
        new_table.append(summ)

    for i in range(len(new_table)):
        temp = table[i].split()

        if maxi < new_table[i]:
            maxi = new_table[i]
            answer = temp[0]

        elif maxi == new_table[i]:
            if answer[0] > temp[0][0]:
                maxi = new_table[i]
                answer = temp[0]

    return answer


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
               ["JAVA", "JAVASCRIPT"], [7,5]))