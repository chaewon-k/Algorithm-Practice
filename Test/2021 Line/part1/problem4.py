from re import compile
def solution(data, word):
    answer = []
    table = [['0']*2 for _ in range(len(data)+1)]

    for d in data:
        temp = d.split()
        table[int(temp[0])][0] = str(temp[1])
        table[int(temp[0])][1] = temp[2]

    word_list = []
    temp_list = []
    start = 0
    for i in range(len(table)):
        if word == table[i][0]:
            word_list.append([table[i][0], i, 1])
            start += 1
        else:
            cnt = len(compile(word).findall(table[i][0]))
            if cnt >= 1:
                temp_list.append([table[i][0], i, cnt])

    temp_list.sort(key= lambda x: (x[0],x[2]))
    word_list.append(temp_list)

    for w in word_list:
        string = w[0]
        idx = w[1]
        answer_list = []
        while idx != 0:
            answer_list.append(string)
            string = table[idx][0]
            idx = int(table[idx][1])

    return answer



print(solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"],
               "BROWN"))
# ["CONY/DOLL/BROWN-CONY", "BROWN/DOLL/LARGE-BROWN", "BROWN/DOLL/SMALL-BROWN"]
print(solution([["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"],
               "SALLY"))
# ["Your search for (SALLY) didn't return any results"]
print(solution(["1 ROOTA 0", "2 AA 1", "3 ZZZ 1", "4 AABAA 1", "5 AAAAA 1", "6 AAAA 1", "7 BAAAAAAA 1", "8 BBAA 1", "9 CAA 1", "10 ROOTB 0", "11 AA 10"],
               "AA"))
# ["ROOTA/AA", "ROOTB/AA", "ROOTA/BAAAAAAA", "ROOTA/AAAAA", "ROOTA/AAAA", "ROOTA/AABAA", "ROOTA/CAA", "ROOTA/BBAA"]