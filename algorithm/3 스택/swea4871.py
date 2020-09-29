import sys
sys.stdin = open('swea4871.txt','r')

T = int(input())

def chk(start,end):

    if end in link.get(start,[0]): # 찾아간 링크 안에 있으면 end값 있으면 1반환
        return 1

    if link.get(start) != None and end not in link.get(start): # 찾아간 링크 안에 end 없고, 링크자체가 존재할 때

        for i in link.get(start): # 그 링크 안에서 다시 체크
            if chk(i,end):
                return 1
    return 0

for tc in range(1,T+1):
    V,E = map(int,input().split())
    input_list=[list(map(int,input().split())) for _ in range(E)]
    start,end = map(int,input().split())
    link={}


    for k,val in input_list: # 링크 만들기
        if link.get(k)==None:
            link[k] = [val]
        else:
            link.get(k).append(val)

    print(f'{tc} {chk(start,end)}')

'''
'''
T = int(input())

def chk(start,end):

    if end in link.get(start,[0]): # 찾아간 링크 안에 있으면 end값 있으면 1반환
        return 1

    if link.get(start) != None and end not in link.get(start): # 찾아간 링크 안에 end 없고, 링크자체가 존재할 때
        for i in link.get(start): # 그 링크 안에서 다시 체크
            if chk(i,end):
                return 1
    return 0

for tc in range(1,T+1):
    V,E = map(int,input().split())
    input_list=[list(map(int,input().split())) for _ in range(E)]
    start,end = map(int,input().split())
    link={}


    for k,val in input_list: # 링크 만들기
        if link.get(k)==None:
            link[k] = [val]
        else:
            link.get(k).append(val)

    print(f'{tc} {chk(start,end)}')