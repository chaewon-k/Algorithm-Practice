from itertools import product
def find_menus(order, bit):
    temp = []
    str_temp = ''
    for b in range(len(bit)):
        if bit[b] == 1:
            temp.append(order[b])
    temp.sort()
    for t in temp:
        str_temp += t
    return str_temp

def find_maxi(dict):
    maxi = 0
    str_list = []
    for key, value in dict.items():
        if value == maxi:
            str_list.append(key)
        elif value > maxi:
            str_list = [key]
            maxi = value
    if maxi < 2:
        str_list = []
    return str_list

def solution(orders, course):
    answer = []
    for c in course:
        dict = {}
        for order in orders:
            length = len(order)
            # 비트 배열 구하기
            bit_arr = list(product([0,1], repeat=length))
            for bit in bit_arr:
                # 비트 배열 합이 2이면 (메뉴가 2개이면)
                if sum(bit) == c:
                    # 문자열 구해서 dict에 넣기
                    menu = find_menus(order, bit)
                    if menu in dict.keys():
                        dict[menu] += 1
                    else:
                        dict[menu] = 1
        # 가장 많은 수의 단어 리스트 찾기
        li = find_maxi(dict)
        for l in li:
            answer.append(l)

    # 오름차순 정렬
    answer.sort()

    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))