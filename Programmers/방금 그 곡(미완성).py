def solution(m, musicinfos):
    answer = ''

    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        start, end = musicinfo[0], musicinfo[1]
        time = int(end[3:]) - int(start[3:])
        if start[:2] != end[:2]:    time += (int(end[:2]) - int(start[:2])) * 60

        i = 0
        letter = ''
        stack = []
        temp = musicinfo[3]
        while i < len(temp):
            if temp[i] == '#':
                letter += temp[i]
                stack.append(letter)
                letter = ''
            else:
                if len(letter) >= 1:
                    stack.append(letter)
                    letter = ''
                    letter += temp[i]
            i += 1
        print(stack)




        print(musicinfo)

    return answer

print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))