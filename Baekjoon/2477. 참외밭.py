N = int(input())
area = [list(map(int, input().split())) for _ in range(6)]

num = [0]*5
for i in area:
    num[i[0]] += 1

sub_area = []
for i in range(len(num)):
    if num[i]==2:
        sub_area.append(i)
sub_length = []
total_area = 1
for i in area:
    direct, length = i
    if direct in sub_area:
        sub_length.append(length)
    else:
        total_area *= length

print(N*(total_area-sub_length[1]*sub_length[2]))