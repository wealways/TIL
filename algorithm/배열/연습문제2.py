# 5개의 정수를 입력받아 부분집합의 합이 0이 되는 것의 갯수를 구해보시오

input_list = list(map(int,input().split()))

N = len(input_list)

for i in range(1<<N):
    temp = []
    for j in range(N):
        if i & (1<<j):
            temp.append(input_list[j])

    if sum(temp) == 0:
        print(temp)
