const sol = (arr,target) => {
  let answer = 0
  let sumV = 0
  let lt = 0
  for(let rt=0;rt<arr.length;rt++){
    sumV +=arr[rt]
    while(sumV>target){
      sumV -= arr[lt]
      lt++
    }
    answer +=(rt-lt+1)
  }
  return answer

}

console.log(sol([1,3,1,2,3],5))