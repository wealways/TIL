
temp_list = [[0]*101 for _ in range(101)]

for _ in range(4):
    a,b,c,d = map(int,input().split())

    for i in range(a,c):
        for j in range(b,d):
            temp_list[j][i] += 1

    cnt = 0
    for i in range(101):
        for j in range(101):
            if temp_list[i][j] >= 1:
                cnt += 1

print(cnt)

