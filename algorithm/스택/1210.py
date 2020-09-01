import sys
sys.stdin = open('1210.txt','r')



for tc in range(1,2):
    tc = int(input())
    input_list = [list(input().split()) for _ in range(100)]

    i=len(input_list)-1
    idx= 0
    while i >=0:
        if i==99:
            for j in range(100):
                if input_list[i][j] == 2:

                    idx = j
                    i -= 1
                    print('여기')
                    break;
        else:
            if input_list[i][idx-1] ==1 or input_list[i][idx+1] ==1:
                idx = idx-1
            else:
                i -= 1
    print(i)