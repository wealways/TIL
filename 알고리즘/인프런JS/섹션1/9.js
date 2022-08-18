const sol = (str) => {
    // let result = ''
    // for(let i in str) {
    //     str[i]==='A'?result+='#':result+=str[i]
    // }
    // for(let x of s){
    //     if(x=='A') answer+='#';
    //     else answer+=x;
    // }

    let result = str
    result = result.replace(/A/g,'#')
    return result
}
console.log(sol('BANANA'))