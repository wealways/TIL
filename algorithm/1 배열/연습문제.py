input_list = [7,4,2,0,0,6,0,7,0]

lenght = len(input_list)
result_list = [0]*lenght

for n, i in enumerate(input_list):

    for j in range(n, lenght):
        if i > input_list[j]:
            result_list[n] +=1

    result = result_list[0]
    for m in result_list:
        if result <= m:
            result = m

print(result)
print(max(result_list),result_list)

maxcnt=0
for i in range(len(input_list)-1):
    cnt = 0
    for k in range(i+1, len(input_list)):
        if input_list[k] < input_list[i]:
                cnt += 1
    if maxcnt < cnt:
        maxcnt = cnt

print(maxcnt)