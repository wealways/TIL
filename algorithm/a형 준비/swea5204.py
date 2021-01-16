import sys
sys.stdin = open('input1.txt')

def merge(left,right):
    global cnt
    idxl = idxr = 0
    res = []
    if left[-1] > right[-1]:
        cnt += 1
    while idxl < len(left) and idxr<len(right):
        if left[idxl] < right[idxr]:
            res.append(left[idxl])
            idxl += 1
        else:
            res.append(right[idxr])
            idxr += 1
    # 왼쪽이 남았으면 왼쪽것은 res에 붙여준다
    # 오른쪽이 남았으면 오른쪽것은 res에 붙여준다
    while idxl < len(left):
        res.append(left[idxl])
        idxl += 1

    while idxr < len(right):
        res.append(right[idxr])
        idxr += 1

    return res
def merge_sort(a):
    if len(a)==1:
        return a
    else:
        m = len(a)//2
        left = merge_sort(a[:m])
        right = merge_sort(a[m:])
        return merge(left, right)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    data = merge_sort(data)
    print('#{} {} {}'.format(tc, data[N//2],cnt))