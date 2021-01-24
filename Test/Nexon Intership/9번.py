def smallestNegativeBalance(debts):
    mem_dict = {}
    for i in debts:
        if i[0] not in mem_dict:
            mem_dict[i[0]] = 0
        if i[1] not in mem_dict:
            mem_dict[i[1]] = 0
        mem_dict[i[0]] -= int(i[2])
        mem_dict[i[1]] += int(i[2])

    mini = 0
    result = []
    for key, value in mem_dict.items():
        if value < mini:
            mini = value
            result = [key]
        elif value == mini:
            result.append(key)

    if mini == 0:
        return ['Nobody has a negative balance']
    return sorted(result)

print(smallestNegativeBalance([['Alex', 'Blake', '2'], ['Blake', 'Alex', '2'], ['Casey', 'Alex', '5'],
                                ['Blake', 'Casey', '7'], ['Alex', 'Blake', '4'],['Alex','Casey','4']]))
print(smallestNegativeBalance([['Alex','Blake','5'], ['Blake','Alex','3'],['Casey', 'Alex', '7'],
                               ['Casey', 'Alex', '4'],['Casey','Alex','2']]))