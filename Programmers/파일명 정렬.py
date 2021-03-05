import re

def solution(files):
    answer = []
    table = []
    for file in files:
        table.append(re.split(r"([0-9]+)", file))
    sort_table = sorted(table, key = lambda x: (x[0].lower(), int(x[1])))

    for i in sort_table:
        answer.append(''.join(i))

    return answer


# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))