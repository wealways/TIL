const sol = (arr) => {
    let maxV = Number.MIN_SAFE_INTEGER
    let result
    for (let a of arr){
        console.log(a.length)
        if(maxV<=a.length) {
            result = a
            maxV = a.length
        }
    }
    return result
}
console.log(sol(["teacher", "time", "student", "beautiful", "good"]))