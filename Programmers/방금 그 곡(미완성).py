def find_song(time, title, queue, word):
    j = 0
    cnt = 0
    total_time = time
    while time >= 1:
        print(queue)
        time -= 1
        temp = queue.pop(0)
        if temp == word[j]:
            cnt += 1
            j += 1
        else:
            cnt = 0
            j = 0
        queue.append(temp)

        if cnt == len(word):
            if total_time - time >= len(queue):
                if queue[0] == word[0]:
                    return True
                else:
                    j = 0
                    cnt = 0
            else:
                return True
    return False


def solution(m, musicinfos):
    answer = ''
    temp = []
    for i in musicinfos:
        temp.append(i.split(','))

    time_info = []
    for i in temp:      # [재생 길이, 제목, 악보] 테이블 만들기
        start = int(i[0][:2])*60 + int(i[0][3:5])
        end = int(i[1][:2])*60 + int(i[1][3:5])
        sound_info = []
        sound = i[3]
        j = 0
        while j < len(sound)-1:
            if sound[j+1] == '#':
                sound_info.append(sound[j:j+2])
                j += 2
            else:
                j += 1
                sound_info.append(sound[j])
                if j == len(i)-2:
                    sound_info.append(sound[j+1])

        time_info.append([end-start, i[2], sound_info])
    #print(time_info)

    max_time = -1
    for i in time_info:
        time, title, sound = i
        if find_song(time,title, sound, list(m))==True and time >= max_time:
            max_time = time
            answer = title

    if answer == '':
        answer = "'(None)'"

    return answer


print(solution(	"ABC", ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))