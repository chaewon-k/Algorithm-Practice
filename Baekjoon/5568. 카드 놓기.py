from itertools import permutations

n = int(input())
k = int(input())
cards = []
for _ in range(n):
    cards.append(input())

arr = list(permutations(cards,r=k))
answer = []
for a in arr:
    result = ''
    for i in a:
        result += i
    answer.append(result)
print(len(set(answer)))

