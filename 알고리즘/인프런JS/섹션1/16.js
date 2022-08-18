const sol = (str) =>{
    let result = ''
    for(let s of str){
        if(result.indexOf(s)==-1) result +=s
    }
    return result
}

console.log(sol('ksekkset'))