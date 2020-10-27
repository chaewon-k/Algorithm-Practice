import sys
sys.stdin=open('sample_input.txt','r')

bit = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
       '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
       'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

ratio_list = {'112': 0, '122': 1, '221': 2, '114': 3, '231': 4, '132': 5, '411': 6, '213': 7, '312': 8, '211': 9}
# 거꾸로된 비율. (뒤에서부터 볼 거라서)

T = int(input())
for t in range(1, T + 1):
    ssum = flag = 0
    final_list = []
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    word_list = [''] * N

    # 각 행 통째로 binary 변환
    for i in range(N):
        for j in range(M):
            word_list[i] += bit[arr[i][j]]

    # 추출
    result_list = []
    for word in word_list:
        bin_list = [0] * 3
        flag = 1
        for w in range(len(word) - 1, -1, -1):
            if word[w] == '1':
                if bin_list[1] == 0 and bin_list[2] == 0:
                    bin_list[0] += 1
                elif bin_list[0] != 0 and bin_list[1] != 0:
                    bin_list[2] += 1
            else:
                if bin_list[0] != 0 and bin_list[2] == 0:
                    bin_list[1] += 1
                elif bin_list[0] != 0 and bin_list[1] != 0 and bin_list[2] != 0:
                    # 비율 나누기
                    mini = min(bin_list)
                    i = 0
                    ratio = ''
                    for i in range(3):
                        bin_list[i] //= mini
                        ratio += str(bin_list[i])
                    result_list.append(ratio_list[ratio])

                    bin_list = [0] * 3

            if len(result_list) == 8:

                result_list = result_list[::-1]
                result = (result_list[0] + result_list[2] + result_list[4] + result_list[6]) * 3 + (
                            result_list[1] + result_list[3] + result_list[5]) + result_list[7]
                if result % 10 == 0 and result_list not in final_list:
                    final_list.append(result_list)
                    ssum += sum(result_list)
                result_list = []
    print(f'#{t} {ssum}')