const dx = [0,0,1,-1]
const dy = [1,-1,0,0]

const sol = (arr) => {
  let cnt = 0
  for(let i=0;i<arr.length;i++){
    for(let j=0;j<arr.length;j++){
      let flag = true
      for(let k=0;k<4;k++){
        let nx = i+dx[i]
        let ny = j+dy[j]
        if(nx>=0 && nx<arr.length && ny>=0 && ny<arr.length){
          if(arr[i][j]<=arr[nx][ny]){
            flag = false
            break
          }
        }
      }
      if(!flag){
        cnt +=1
      }
    }
  }
  return cnt
}

let arr=[[5, 3, 7, 2, 3], 
        [3, 7, 1, 6, 1],
        [7, 2, 5, 3, 4],
        [4, 3, 6, 4, 1],
        [8, 7, 3, 5, 2]];
console.log(sol(arr));