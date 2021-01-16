inputNum = int(input())
arr = [0] * (inputNum + 1)

for i in range(1, inputNum + 1):
    if i == 1:
        continue
    values = []
    if i % 3 == 0:
        values.append(arr[i//3] + 1)
    if i % 2 == 0:
        values.append(arr[i//2] + 1)
    values.append(arr[i-1] + 1)
    arr[i] = min(values)

print(str(arr[inputNum]))
