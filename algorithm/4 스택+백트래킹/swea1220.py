import sys
sys.stdin = open('swea1220.txt','r')

# 1은 N / 2는 S  위엔 N 아래는 S
# 위 아래라는 특성상, 1이오고 그 다음에 2가 와야  교착상태가 하나 발생
for tc in range(1,11):
    N = int(input())
    input_list = [list(map(int,input().split())) for _ in range(N)]
    trans = list(map(list, zip(*input_list)))
    cnt = 0
    for y in range(100):
        temp = 0
        for x in trans[y]:
            if x == 1:
                temp +=1
            if x==2 and temp>=1:
                cnt += 1
                temp = 0
    print(f'#{tc} {cnt}')