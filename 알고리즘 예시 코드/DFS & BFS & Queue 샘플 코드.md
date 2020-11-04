# DFS 



### 1. stack 을 사용하는 dfs

#### (1) 방향X & 인접행렬 X & stack

```python
def dfs(s, V): # 반복구조의 깊이우선탐색
    # 초기화, 스택생성, visited[] 생성 및 초기화
    visited = [0]*(V+1) # visited[] 생성
    #stack = [s]  # 스택생성, 시작노드 push()
    stack = []
    stack.append(s) # push()
    visited[s] = 1
    while stack: # 스택이 비어있지 않으면 반복
        n = stack.pop() # 탐색할 노드 선택. pop()
        for i in range(1, V+1): # n에 인접하고 방문안한 노드 찾기
            if adj[n][i]==1 and visited[i] == 0: # i가 n에 인접하고 미방문이면
                stack.append(i)
                visited[i] = 1

V, E = map(int, input().split()) # V 정점 개수, E 간선 개수
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
tmp = list(map(int, input().split())) # E개의 간선 정보
for i in range(E): # 인접행렬 기록
    n1 = tmp[i*2]
    n2 = tmp[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 무방향 그래프인 경우

dfs(1, V)
```



#### (2) (3) 방향 0 & 인접행렬 & stack

```python
def f2(stx, goal, V): # dfs 반복
    stack = [] # 스택생성
    stack.append(stx) # 시작점 push
    v = [0]*(V+1)   # 방문 기록

    while stack: # 탐색할 노드가 남아있으면 반복
        n = stack.pop()
        if v[n]==0: # 방문한 노드인지 확인
            v[n] = 1
            if n==goal:
                return 1 # 목적지에 도착할 수 있는 경우
            for i in range(1, V+1):
                if adj[n][i]==1: # n노드에 인접하고 미방문인 i노드가 있으면
                    stack.append(i)
    return 0 # 목적지에 도착하지 못하고, 가능한 모든 노드를 방문한 경우


def f1(stx, goal, V): # dfs 반복
    stack = [] # 스택생성
    stack.append(stx) # 시작점 push
    v = [0]*(V+1)   # 방문 기록
    v[stx] = 1      # 시작점 방문 표시
    while stack: # 탐색할 노드가 남아있으면 반복
        n = stack.pop()
        if n==goal:
            return 1 # 목적지에 도착할 수 있는 경우
        for i in range(1, V+1):
            if adj[n][i]==1 and v[i]==0: # n노드에 인접하고 미방문인 i노드가 있으면
                stack.append(i)
                v[i] = 1
    return 0 # 목적지에 도착하지 못하고, 가능한 모든 노드를 방문한 경우

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬 생성
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1 # 방향 그래프
    stx, goal = map(int, input().split())

    #print(f'#{tc} {f1(stx, goal, V)}')
    print(f'#{tc} {f2(stx, goal, V)}')
```



### 2. 재귀를 사용한 DFS

```python
def f3(n, goal, V): # dfs 재귀
    visited[n] = 1 # 현재 방문한 노드에 방문표시
    if n == goal: #목적지에 방문한 경우
        return 1    #  목적지에 도착했음을 알림
    else:
        for i in range(1, V+1):
            if adj[n][i]==1 and visited[i]==0: # n에 인접하고 미방문인 i가 있으면
                if f3(i, goal, V):          # i로 이동
                    return 1            # 목적지를 찾은 상태로 리턴하면 탐색 중지
        return 0    # 인접 노드가 없거나 인접노드 이동 후 목적지를 못 찾은 경우



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬 생성
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1 # 방향 그래프
    stx, goal = map(int, input().split())


    visited = [0]*(V+1)
    print(f'#{tc} {f3(stx, goal, V)}')
```



---------------------------

# BFS 

### 1. Queue 를 이용한 BFS

```python
def BFS(v):
    # 큐, 방문
    Q = []
    visit = [0]*(V+1)

    #enQ(v), visit(v)
    Q.append(v)
    visit[v] = 1
    # 큐가 비어있지 않을 동안
    while Q:
    	#v = deQ()
        v = Q.pop(0)
        #v의 인접한 정점(w), 방문 안한 정점이면
            for w in range(1, V+1):
            if G[v][w] == 1 and visit[w] == 0:
                Q.append(w)
                visit[w] = 1
                print(w, end = " ")
```



#### (1) 인접 리스트를 이용한 BFS (방향 없는 그래프)

```python
def bfs(v):
    Q = []
    visit = [0] * (V+1)
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = 1

V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[] for _ in range(V+1)]
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s].append(e)
    G[e].append(s)
bfs(1)
```





-----------------------

# Heap 



### 1. Heap 직접 구현

```python
def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount  # 입력된 수의 위치
    parent = cur//2

    #루트가 아니고, if 부모노드 값 > 자식노드 값 이면 swap
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2

def heappop():
    global heapcount
    returnValue = heap[1]
    heap[1] = heap[heapcount]
    heap[heapcount] = 0
    heapcount -= 1

    parent = 1
    child = parent * 2		#왼쪽 자식이라 두자

    if child + 1 <= heapcount:      #오른쪽 자식 존재하면,
        if heap[child] > heap[child+1]:
            child += 1
    #자식 노드가 존재하고, 부모노드 > 자식노드 면, swap
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent *2
        if child + 1 <= heapcount:
            if heap[child] > heap[child+1]:     #오른쪽 자식 존재
                child += 1
    return returnValue

# 완전이진트리!!
# minheap
temp = [7,2,5,3,4,6]
heapcount = 0
N = len(temp)
heap = [0]*(N+1)
for i in range(N):
    heappush(temp[i])
print(heap)

for i in range(N):
    print(heappop(), end = " ")
print()
```



### 2. library 이용한 Heap

```python
import heapq
heap = [7,2,5,3,4,6]
heapq.heapify(heap)
heapq.heappush(heap, 1)
while heap:
    print(heapq.heappop(heap), end = ' ')

#최대힙으로 나타내기
temp = [7,2,5,3,4,6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i],temp[i]))
heapq.heappush(heap2, (-1,1))

while heap2:
    print(heapq.heappop(heap2)[1],end = ' ')
```

