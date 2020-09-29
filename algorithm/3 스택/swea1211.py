import sys
sys.stdin = open('swea1211.txt','r')

for tc in range(1, 11):
    tc = int(input())
    input_list = [list(map(int, input().split())) for _ in range(100)]

    start=[]
    for i,n in enumerate(input_list[0]):
        if n==1:
            start.append(i)

    flag=0

    minv=999999
    for i in start:
        x=i
        y = 0
        cnt = 1
        while y<=99:
            if x <99 and input_list[y][x+1]==1 and flag>-1:
                x = x+1
                flag += 1
                cnt += 1
            elif x>0 and input_list[y][x-1]==1 and flag<1:
                x = x-1
                flag -= 1
                cnt += 1
            else:
                y += 1
                flag = 0
                cnt +=1
        if minv >= cnt:
            minv=cnt
            ans=i
    print(f'#{tc} {ans}')




#
# def chk(y,x):
#     visited.append((y,x))
#
#     if y==0:
#         result.append(x)
#         return
#
#     for i in range(3):
#         newy = y + dy[i]
#         newx = x + dx[i]
#         if 0<= newy <=99 and 0<=newx<= 99:
#             if input_list[newy][newx] == 1 and (newy,newx) not in visited:
#                 chk(newy,newx)
#
#
# for tc in range(1, 11):
#     tc = int(input())
#     input_list = [list(map(int, input().split())) for _ in range(100)]
#
#     start_y = 99
#     dy = [0, 0, -1]
#     dx = [-1, 1, 0]
#
#     start=[]
#     minV=99999999999
#     for i,n in enumerate(input_list[99]):
#         if n==1:
#             start.append(n)
#
#     for i in start:
#         start_x = i
#         result = []
#         visited = []
#         chk(start_y, start_x)
#
#         if minV >= len(visited):
#             minV=len(visited)
#             ans = result[0]
#
#     print(ans)
# #
