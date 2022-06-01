const sol = (n) => {
    let ans = 0
    for(let i =1 ;i<=n;i++){
        ans +=i
    }
    return ans
}

console.log(sol(6))