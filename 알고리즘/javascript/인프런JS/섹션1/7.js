const sol = (n,arr) =>{
    let ans = 0
    for(let a of arr){
        a%10==n?ans+=1:null
    }
    return ans
}

console.log(sol(3,[25,23,11,47,53,17,33]))
console.log(sol(0,[12,20,54,30,87,91,30]))