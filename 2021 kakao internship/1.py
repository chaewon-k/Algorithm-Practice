import itertools
m = 2
w = 2

men_list = []
women_list = []

for i in range(1, m+1):
    men_list.append(i)
for i in range(1, w+1):
    women_list.append(i)

pick_women = list(itertools.combinations(women_list,2))
pick_men = list(itertools.combinations(men_list,2))

print(m*len(pick_women) + w*len(pick_men))