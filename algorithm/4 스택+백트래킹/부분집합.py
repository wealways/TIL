def subG(k):
    if k==N:
        print(S)
        for i in range(N):
            if S[i]==1:
                print(lst[i],end=' ')
        print()
    else:
        S[k]= 0
        subG(k+1)
        S[k]=1
        subG(k + 1)
N=3
lst=[1,3,5]
S=[-1]*N
subG(0)