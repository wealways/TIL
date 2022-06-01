const sol = (str) => {
    let result = ''
    for(let s of str){
        s === s.toUpperCase()?result += s.toLowerCase() : result+= s.toUpperCase()
    }
    return result
}

console.log(sol('StuDY'))