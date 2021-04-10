from collections import deque

def solution(numbers, target):
    answer = 0
    N = len(numbers)
    queue = deque([(0, 0)])  # ([(cnt, sum)])

    while queue:
        cnt, ssum = queue.popleft()
        if cnt > N:
            break
        elif cnt == N and ssum == target:
            answer += 1

        queue.append((cnt + 1, ssum + numbers[cnt - 1]))
        queue.append((cnt + 1, ssum - numbers[cnt - 1]))

    return answer