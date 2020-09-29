

arr = [1,2,3]
N = len(arr)
for i in range(1<<N):
    for j in range(N): # 데이터 개수 만큼

        if i & (1<<j): # j번째 비트가 1이면
            print(arr[j], end=' ')

            # 데이터 합
    print()
        # if # 합이 0이냐??
