const sol = (arr) =>{
    let sumV = 0,minV = Number.MAX_SAFE_INTEGER
    for(let a of arr){
        if(a%2==1) {
            sumV += a
            if(minV>=a) minV= a
        }
    }

    return [sumV,minV]
}

console.log(sol([12,77,38,41,53,92,85]))