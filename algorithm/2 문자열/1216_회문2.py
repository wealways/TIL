import sys
sys.stdin = open('1216.txt','r')

def chk(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-1-i]:
            return False
    return True

for tc in range(1,11):
    tc = int(input())
    texts =[list(input()) for _ in range(100)]

    maxV = 0
    for x in range(100):
        text = []
        text_t = []
        for y in range(100):
            text.append(texts[y][x])
            text_t.append(texts[x][y])

        for m in range(1,100):
            i = 0
            while m+i <= 100:
                arr1 = text[0+i:m+i]
                arr2 = text_t[0+i:m+i]
                if chk(arr1):
                    if maxV <= len(arr1):
                        maxV = len(arr1)
                    m += 1
                    break;

                if chk(arr2):
                    if maxV <= len(arr2):
                        maxV = len(arr2)
                    m += 1
                    break;

                i += 1

    print('#{} {}'.format(tc, maxV))




