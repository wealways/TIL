const sol = (arr) => {
    let minV = Number.MAX_SAFE_INTEGER;
    arr.forEach(a => {
        if(minV>=a){
            minV=a
        }
    });
    // minV = Math.min(...arr)
    // minV = Math.min.apply(null,arr)
    return minV
}

console.log(sol([5,3,7,11,2,15,17]))