def change_to_sec(time):
    return int(time[:2])*60*60 + int(time[3:5])*60 + int(time[6:])

def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    play_time_sec = change_to_sec(play_time)
    runtime = [0] * (play_time_sec + 1)

    adv_time_sec = change_to_sec(adv_time)

    for log in logs:
        temp = log.split('-')
        start = change_to_sec(temp[0])
        end = change_to_sec(temp[1])
        runtime[start] += 1
        runtime[end] -= 1

    for i in range(1, play_time_sec+1): # x 부터 x+1 까지 1초 동안의 재생시간
        runtime[i] += runtime[i-1]

    for i in range(1, len(runtime)):
        runtime[i] += runtime[i-1]      # 0 부터 x+1 까지의 누적 재생시간

    most_view = max_time = 0
    for i in range(adv_time_sec - 1, play_time_sec):        # 처음부터 광고가 시작한다고 가정했을 때의 끝나는 시간
        if i >= adv_time_sec:
            if most_view < runtime[i] - runtime[i - adv_time_sec]:  # 시청자 수가 많은 경우 갱신
                most_view = runtime[i] - runtime[i - adv_time_sec]
                max_time = i - adv_time_sec + 1                     # 시청 시간도 갱신
        else:
            if most_view < runtime[i]:
                most_view = runtime[i]
                max_time = i - adv_time_sec + 1

    return int_to_str(max_time)

# "01:00:00"
# print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))