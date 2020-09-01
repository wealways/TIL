import sys
sys.stdin=open('1219.txt','r')

def f1(n): # n번 노드 방문
    global ans
    if n>=0:
        if n==99:
            ans = 1
        f1(ch1[n])
        f1(ch2[n])

for _ in range(10):
    tc, E = map(int,input().split())
    temp = list(map(int,input().split()))
    ch1 = [-1]*100   #출발점을 인덱스로 도착점 번호를 저장
    ch2 = [-1]*100

    for i in range(E):
        s = temp[i*2]   #출발노드
        e = temp[i*2+1] #도착노드
        if ch1[s] == -1:   #첫 도착지일 경우
            ch1[s] = e
        else:           #두번째 도착지일 경우
            ch2[s] = e
    ans = 0
    f1(0)
    print(f'#{tc} {ans}')
