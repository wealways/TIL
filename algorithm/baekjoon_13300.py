N, K =map(int,input().split())
result = 0
cnt = [0]*12
#i 0 2 4 6 8 10  // 1 3 5 7 9 11
#n 1 2 3 4 5 6      1 2 3 4 5 6
# 2*(n-1)           2*n-1


for _ in range(N):
    s, y = map(int, input().split())
    if s:
        cnt[(2*y)-1] += 1
        if cnt[(2*y)-1] == K:
            cnt[(2 * y) - 1] = 0
            result += 1
    else:
        cnt[2*(y-1)] += 1
        if cnt[2*(y-1)] == K:
            cnt[2 * (y - 1)] = 0
            result += 1

for n in cnt:
    if n!=0:
        result += 1

print(cnt)
print(result)
