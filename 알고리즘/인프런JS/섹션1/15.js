const sol = (str) =>{
    const idx=Math.floor(str.length/2)
    if(str.length%2==0){
        // return str[idx-1]+str[idx]
        return str.substring(idx-1,idx+1)
    }  else{
        return str.substr(idx,1)
    }
}

console.log(sol('study'))
console.log(sol('good'))