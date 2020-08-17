
N = int(input())
input_list = list(map(int, input().split()))


result = []
for i, n in enumerate(input_list):
    result.insert(i-n, i+1)


print(result)
