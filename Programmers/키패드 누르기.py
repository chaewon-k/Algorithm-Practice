def solution(numbers, hand):
    answer = ''
    queue = []
    num_list = [[1,4,7],[2,5,8,0],[3,6,9]]
    for num in numbers:
        if num in num_list[0]:  queue.append((num_list[0].index(num),0))
        elif num in num_list[1]:    queue.append((num_list[1].index(num),1))
        else:   queue.append((num_list[2].index(num),2))

    now_left = (3,0)
    now_right = (3,2)

    for num in queue:
        if num[1] == 0:
            answer += 'L'
            now_left = num

        elif num[1] == 2:
            answer += 'R'
            now_right = num
        else:
            dist_left = abs(now_left[0]-num[0])+abs(now_left[1]-num[1])
            dist_right = abs(now_right[0] - num[0]) + abs(now_right[1] - num[1])

            if dist_left < dist_right:
                answer += 'L'
                now_left = num
            elif dist_left > dist_right:
                answer += 'R'
                now_right = num
            else:
                if hand == 'right':
                    answer += 'R'
                    now_right = num
                else:
                    answer += 'L'
                    now_left = num
    return answer

solution([1,3,4,5,8,2,1,4,5,9,5], 'right')
# LRLLLRLLRRL