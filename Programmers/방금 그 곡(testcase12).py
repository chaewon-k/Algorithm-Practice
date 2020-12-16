def change(temp):
    i = 0
    stack = []
    while i < len(temp) - 1:
        if temp[i + 1] == '#':
            stack.append(temp[i:i + 2])
            i += 2
        elif temp[i + 1] != '#' and temp[i] != '0':
            stack.append(temp[i])
            i += 1
    return stack

def solution(m, musicinfos):
    answer = ''
    max_time = 0

    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        start, end = musicinfo[0], musicinfo[1]
        time = int(end[3:]) - int(start[3:])
        if start[:2] != end[:2]:    time += (int(end[:2]) - int(start[:2])) * 60

        sounds = change(musicinfo[3] + '0')
        code = change(m+'0')
        if time > len(sounds):
            sounds *= (time//len(sounds))+1

        i = j = cnt = 0
        while j+len(code) < time:
            if code[i] == sounds[j]:
                cnt += 1
                i += 1
            else:
                cnt = 0
                i = 0
            if cnt == len(code):
                if max_time < time:
                    max_time = time
                    answer = musicinfo[2]
                break
            j += 1

    if len(answer) == 0:    answer = "(None)"

    return answer

print(solution("cdcdf",["00:00,00:07,ok,cdcdcdf"]))     # cdcd비교하고 f에서 틀리면 이전으로 돌아가야하는데, 내 코드는 돌아가지 않도록 설정함..

# print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))