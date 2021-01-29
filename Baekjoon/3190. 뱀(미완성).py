N = int(input())
arr = [[0]*N for _ in range(N)]
apple_num = int(input())
for i in range(apple_num):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
site_num = int(input())
site_list = []
for i in range(site_num):
    a,b = map(int, input().split())
    site_list.append([a,b])

x = y = d = cnt = 0
time, way = site_list.pop(0)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

dir = (dir + 1) % 4 if r == 'D' else (dir + 3) % 4

while True:

    if time == cnt:


    cnt += 1


