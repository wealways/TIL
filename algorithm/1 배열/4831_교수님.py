def  find(v,k,n,m):
    v.insert(0,0)   #출발점과 종점 번호 추가
    v.append(n)

    last = 0        # 마지막 충전기
    cnt = 0         # 충전 횟수

    for i in range(1,m+2):
        if(v[i]-v[i-1])>k:  # 충전기 사이가 k보다 멀 때
            return 0
        if v[i] > last + k: # 충전기까지 갈 수 없으면
            last=v[i-1]     # 이전 충전기에서 충전
            cnt += 1
    return cnt              # 최소 충전 횟수