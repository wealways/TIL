const sol = (arr,target) => {
  let answer = 0
  let sumV = 0
  let lt = 0
  for(let rt=0;rt<arr.length;rt++){
    sumV += arr[rt]
    if(sumV == target) answer+=1
    while(sumV>=target) {
      sumV -= arr[lt]
      lt+=1
      if(sumV==target) answer+=1
    }
  }
  return answer
}
let arr=[1, 2, 1, 3, 1, 1, 1, 2];
console.log(sol(arr,6));