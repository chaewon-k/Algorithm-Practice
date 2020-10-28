# 순열
def perm(n, k):
    if n==k:
        print(A)
    else:
        for i in range(n,k):
            A[n], A[i] = A[i], A[n] # 현재 숫자부터 오른쪽 끝까지 교환
            perm(n+1,k)             # 다음자리 결정하러 이동
            A[n], A[i] = A[i], A[n] # 교환 전으로 복구

A = [1,2,3]
perm(0,3)

# 부분집합 생성
arr = [3,6,7,1,5,4]
n = len(arr)

for i in range(0,(1<<n)):   # 부분집합의 개수
    for j in range(0,n):    # 원소의 수만큼 비트를 비교
        if i & (1<<j):      # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j])
    print()


# 조합
def f(n,s,N,r): # n: c[n]조합의 인덱스, s: 선택구간의 시작, N: 주어진 개수, r: 고를 개수
    if n==r:
        print(c)
    else:
        for i in range(s, N-r+n+1):
            c[n] = i
            f(n+1, i+1, N, r)

N = 10
r = 3
c = [0]*3
f(0,0,N,r)

