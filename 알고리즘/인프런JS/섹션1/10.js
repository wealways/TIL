const sol = (str,target) => {
    // let result = 0
    // for(let s of str){
    //     if(s===target) result+=1
    // }
    // return result

    return str.split(target).length - 1
}

console.log(sol('COMPUTERPROGRAMMING','R'))