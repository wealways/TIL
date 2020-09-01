import sys
sys.stdin = open('4865.txt','r')

T = int(input())

for tc in range(1,T+1):
    str1 = list(input())
    str2 = list(input())

    dict2={}
    for s in str2:
        if dict2.get(s,0)==0:
            dict2[s] = 1
        else:
            dict2[s] += 1
    maxV= 0
    for s in set(str1):
        if maxV <= dict2.get(s):
            maxV = dict2.get(s)
    print('#{} {}'.format(tc,maxV))


'''
a= [1,2,3,3,3]
d={}
for i in a:
    if d.get(i)==None:
       d[i]=d.get(i,1)
    else:
        d[i] += 1
print(d)
'''