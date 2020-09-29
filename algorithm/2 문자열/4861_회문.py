import sys
sys.stdin=open('4861.txt','r')

#팰린드롬 체크 하는 함수
def palin(arr):
    # 반으로 나눠서 양 끝에서부터 비교
    for i in range(len(arr)//2):
        if arr[i] !=arr[len(arr)-1-i]:
            return False
    return True


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    texts = [list(input()) for _ in range(N)]

    # 팰린드롬을 확인할 크기
    m = M

    # 가로 세로로 모두 확인할 수 있다고 했기 때문에, 가로세로 각각의 회문 check
    for idx_y in range(N):

        # text= 가로 / text_t= 세로
        text=[]
        text_t=[]
        for idx_x in range(N):
            text.append(texts[idx_y][idx_x])
            text_t.append(texts[idx_x][idx_y])

        #N이 M보다 클 수 있기 때문에, i를 활용해서 N
        i = 0
        while m+i <=N:
            if palin(text[0+i:m+i]):
                print('#{} {}'.format(tc,text[0+i:m+i]))
                break
            elif palin(text_t[0+i:m+i]):
                print('#{} {}'.format(tc, text_t[0+i:m+i]))
                break
            else:
                i += 1
