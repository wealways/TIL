const sol = (arr) => {
    // let maxV = Number.MIN_SAFE_INTEGER
    // for(let x of arr) {
    //     if(maxV<x){
    //         console.log(x)
    //     }
    //     maxV = x
    // }
    let answer = [];
    answer.push(arr[0])
    for(let i = 1;i<arr.length;i++){
        if(arr[i]>arr[i-1]) answer.push(arr[i])
    }
    console.log(answer)
}

sol([7,3,9,5,6,12])
