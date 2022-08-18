const solution = (a,b,c) =>{
    let ans = 'YES', maxV
    let total = a+b+c
    if(a>b) maxV = a
    else maxV = b
    if(c>maxV) maxV =c 

    if(total-maxV<=maxV) ans = 'NO'
    return ans
} 

console.log(solution(13,33,17))