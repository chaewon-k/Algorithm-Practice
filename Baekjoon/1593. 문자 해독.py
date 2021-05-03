W_len, S_len = map(int, input().split())
W = input()
S = input()
dict_all = {}
dict_temp = {}
for i in W:
    if i in dict_all:
        dict_all[i] += 1
    else:
        dict_all[i] = 1
        dict_temp[i] = 0

i = j = 0
while True:
    if j-i < W_len:
        if S[j] in dict_all


        j += 1


