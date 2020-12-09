from itertools import permutations

def compare(banned_id, user, len_banned_id):
    for i in range(len_banned_id):
        if len(banned_id[i]) != len(user[i]):
            return False
        for j in range(len(user[i])):
            if banned_id[i][j] != '*' and user[i][j] != banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    len_banned_id = len(banned_id)
    user_id_permu = permutations(user_id, len_banned_id)
    for user in user_id_permu:
        if compare(banned_id, user, len_banned_id) == True:
            user = sorted(list(user))
            if user not in answer:
                answer.append(user)
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
               ["fr*d*", "*rodo", "******", "******"]))