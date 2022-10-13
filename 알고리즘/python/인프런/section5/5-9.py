import sys
sys.stdin = open("in4.txt")

data1 = {}
for i in input():
    data1[i]=data1.get(i,0)+1
data2 = {}
for i in input():
    data2[i]=data2.get(i,0)+1

ans = 'YES'
for i in data1:
    if data1[i] != data2[i]:
        ans = 'NO'
        break

print(ans)

