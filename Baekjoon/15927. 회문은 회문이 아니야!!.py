def is_palin(temp):
    left = 0
    right = len(temp) - 1 - left
    while left < right:
        if temp[left] != temp[right]:   return 0
        left += 1
        right -= 1
    a = set(list(temp))
    if len(a) == 1: return -1
    return 1

data = input()
if is_palin(data) == 0:
    print(len(data))
elif is_palin(data) == -1:
    print('-1')
else:
    print(len(data)-1)