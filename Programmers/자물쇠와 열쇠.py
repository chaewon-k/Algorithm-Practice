def make_padding(key,key_s):
    arr = [[0] * (key_s*3) for _ in range(key_s*3)]

    for i in range(key_s):
        for j in range(key_s):
            arr[i+key_s][j+key_s] = key[i][j]

    return arr

def rotation(arr,len_arr):
    return list(zip(*arr[::-1]))

def solution(key, lock):
    answer = True
    key_size = len(key); lock_size = len(lock)

    # 1. key padding 만들기
    key_padding = make_padding(key,key_size)

    for d in range(4):
        # 2. 90도씩 회전
        key_padding = rotation(key_padding, key_size)










    return answer

solution([[0,0,0],[1,0,0],[0,1,1]], [[1,1,1],[1,1,0],[1,0,1]])