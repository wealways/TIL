const sol = arr => {
  let result = Number.MIN_SAFE_INTEGER
  let sumXY = 0
  let sumYX = 0
  for(let i=0;i<arr.length;i++){
    let sumX = 0
    let sumY = 0
    for(let j=0;j<arr.length;j++){
      sumX += arr[i][j]
      sumY += arr[j][i]
      if(i==j){
        sumXY += arr[i][j]
        sumYX += arr[j][i]
      }
    }
    result = Math.max(result,sumX,sumY)
  }
  return result = Math.max(result,sumXY,sumYX)
}


let arr=[[10, 13, 10, 12, 15], 
        [12, 39, 30, 23, 11],
        [11, 25, 50, 53, 15],
        [19, 27, 29, 37, 27],
        [19, 13, 30, 13, 19]];
console.log(sol(arr));