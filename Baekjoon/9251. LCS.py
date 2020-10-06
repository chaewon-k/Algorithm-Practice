string1 = input()
string2 = input()
len1 = len(string1)
len2 = len(string2)

matrix = [[0] * (len2+1) for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1, len2+1):
        if string1[i-1] == string2[j-1]:
            matrix[i][j] = matrix[i-1][j-1]+1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
print(matrix[-1][-1])