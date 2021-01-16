import sys
sys.stdin  = open('swea1240.txt')

code = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    datas = [list(input()) for _ in range(N)]
    # 암호코드가 있는 위치 찾기
    idx = 0
    realcode = []
    for data in datas:
        for i, d in enumerate(data[::-1]):
            if d =='1':
                idx = i
                break
        idx = M-idx+1-56
        print(idx)
        for i in range(7):
            temp = ''.join(data[idx+7*i:idx+7*(i+1)])
            if temp in list(code.keys()):
                realcode.append(code[temp])
        if len(realcode):
            break

    print(realcode)