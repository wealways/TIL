def per(k):
    if k==N:
        print(s)
        for ss in s:
            print(lst[ss],end=' ')
        print()

    else:
        for i in range(N):
            if not visited[i]:
                s[k]=i
                visited[i]=True
                per(k+1)
                visited[i]=False




lst=[1,5,10]
N=len(lst)
s=[0]*N
visited=[False]*N
per(0)