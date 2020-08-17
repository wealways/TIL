
N = int(input())
input_list = list(map(int, input().split()))
result = [0]*N

for i, n in enumerate(input_list):
    for j, m in result[:i-n+1]:
        result[j-m] = n

print(result)
