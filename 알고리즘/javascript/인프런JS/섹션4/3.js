const sol = (arr) => {
  let m = arr.length
  let n = arr[0].length

  // 모든 경우의 수
  let result = []
  for(let i=0;i<n;i++){
    for(let j=i+1;j<n;j++){
      result.push([arr[0][i],arr[0][j]])
    }
  }
  // 조건 미충족 경우 제거
  let answer = []
  for(let r of result){
    let x = r[0]
    let y = r[1]
    let flag = true
    for(let i =1; i<m;i++){
      let tx = arr[i].indexOf(x)
      let ty = arr[i].indexOf(y)
      if(tx>=ty) flag = false
    }
    if(flag) answer.push([x,y])
  }
  return answer
}

console.log(sol([[3, 4, 1, 2], [4, 3, 2, 1], [3, 1, 4, 2]]))