import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
K = int(input())

arr = list(map(int,input().split()))

arr.sort()

temp = []
for i in range(1,N):
    temp.append(arr[i]-arr[i-1])
temp.sort()
print(sum(temp[:N-K]))