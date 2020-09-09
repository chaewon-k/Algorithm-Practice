def delete(arr, ans):
    if len(arr) > 1 and arr[len(arr) - 1] == arr[len(arr) - 2]:
        arr.pop(len(arr) - 1)
        arr.pop(len(arr) - 1)
        ans += 2
    return arr, ans


def solution(board, moves):
    answer = 0
    length = len(board)
    new = []
    idx = [length - 1] * length
    for i in range(length):
        for j in range(length):
            if board[i][j] != 0 and idx[j] > i:
                idx[j] = i

    for i in moves:
        j = i - 1
        if idx[j] < length and board[idx[j]][j] != 0:
            new.append(board[idx[j]][j])
            board[idx[j]][j] = 0
            new, answer = delete(new, answer)
            if idx[j] < length - 1: idx[j] += 1
        else:
            continue

    return answer