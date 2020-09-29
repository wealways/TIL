import sys
sys.stdin = open('swea4873.txt','r')


def chk(arr):
    top = 0
    for i in arr:
        if len(s)==0:
            s.append(i)
        else:
            if s[top] != i:
                s.append(i)
                top += 1
            else:
                s.pop(top)
                if top != 0:
                    top -= 1
    return s

T= int(input())
for tc in range(1,T+1):
    input_list = list(input())
    s = list()

    print(f'#{tc} {len(chk(input_list))}')


'''

def chk(arr):
    if len(arr)>1:
        for i in range(1,len(arr)):
            t1= arr[i-1]
            t2=arr[i]
            if t1==t2:
                arr.remove(t1)
                arr.remove(t2)
                break;
            if i == len(arr)-1:
                return arr
        chk(arr)
    return arr

T= int(input())
for tc in range(1,T+1):
    input_list = list(input())
    print(f'#{tc} {len(chk(input_list))}')

'''