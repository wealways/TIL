const sol = (arr,target) => {
  let answer = 0
  // 정렬이 필요하다.
  arr.sort((a,b)=>(a[0]+a[1]-(b[0]+b[1])))
  for(let i=0;i<arr.length;i++){
    let money = target - (arr[i][0]/2 + arr[i][1])
    let cnt = 1
    for(let j=0;j<arr.length;j++){
      if(i!=j && arr[j][0]+arr[j][1]>money) break
      if(i!=j && arr[j][0]+arr[j][1]<=money) {
        money -= arr[j][0]+arr[j][1]
        cnt+=1
      }
    }
    answer = Math.max(answer,cnt)
  }

  return answer
} 

let arr=[[6, 6], [2, 2], [4, 3], [4, 5], [10, 3]];
console.log(sol(arr,28));