N = int(input())
input_list = list(map(int,input().split()))
max_up = 1
max_down = 1

cnt = 1
for i in range(N-1):
    if input_list[i] <= input_list[i+1]:
        cnt += 1
    else:
        cnt = 1
    if max_up <= cnt:
        max_up = cnt

cnt = 1
for i in range(N-1):
    if input_list[i] >= input_list[i+1]:
        cnt += 1
    else:
        cnt = 1
    if max_down <= cnt:
        max_down = cnt

if max_up<=max_down:
    print(max_down)
else:
    print(max_up)