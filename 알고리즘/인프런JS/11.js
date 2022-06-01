const sol = (str) => {
    let result = 0
    for(let s of str){
        if(s === s.toUpperCase()) result +=1
    }
    return result
}

console.log(sol('KoreaTimeGood'))