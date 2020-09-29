
N = int(input())

temp_list = [n for n in range(1, N+1)]


ans_list=[]
for temp in temp_list:
    result = 0
    result_list = [N]
    n=0
    while True:
        d1 = result_list[n]-temp
        if d1<0:
            break;
        result_list.append(d1)
        n += 1
    if len(ans_list) <= len(result_list):
        ans_list = result_list
print(ans_list)
print(len(ans_list))