const sol = (arr) => {
    let result = 1
    let maxV = arr[0]
    for(let i=1;i<arr.length;i++){
        if(maxV<arr[i]){
            result +=1
            maxV = arr[i]
        }
    }
    console.log(result)
}

sol([130,135,148,140,145,150,150,153])