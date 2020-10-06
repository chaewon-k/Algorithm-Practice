string1 = input()
string2 = input()
str2_len = len(string2)
v = [0] * len(string1)
del_cnt = 0
cnt = 0

for i in range(len(string1)):
    if string1[i] in string2 and v[i] == 0:
        v[i] = 1
        cnt += 1
        string2 = string2.replace(string1[i],'',1)
    else:
        del_cnt += 1
del_cnt += (str2_len - cnt)
print(del_cnt)
