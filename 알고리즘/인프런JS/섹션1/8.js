const sol = (arr) => {
    let result = arr
    let sumV = result.reduce((acc,v)=> acc+v,0)
    console.log(sumV)
    for(let i=0;i< 8;i++){
        for(let j=i+1;j<9;j++){
            if(sumV - result[i]-result[j] == 100){
                result.splice(j,1)
                result.splice(i,1)
            }
        }
    }
    return result
}
console.log(sol([20, 7, 23, 19, 10, 15, 25, 8, 13]))