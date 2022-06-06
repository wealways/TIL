const sol = (arr,k) => {
  let answer = Number.MIN_SAFE_INTEGER
  let lt = 0
  for(let lt=0;lt<arr.length-k+1;lt++){
    let temp =0
    for(let i=lt;i<lt+k;i++){
      temp+=arr[i]
    }
    answer = Math.max(answer,temp)
  }
  return answer
}

console.log(sol([12,15,11,20,25,10,20,19,13,15],3))

const sol2 = (arr,k) => {
  let sumV = 0
  for(let i=0;i<k;i++) sumV += arr[i]
  let answer = sumV
  for(let i=k;i<arr.length;i++){
    sumV += (arr[i] - arr[i-k])
    answer = Math.max(answer,sumV)
  }
  return answer
}
console.log(sol2([12,15,11,20,25,10,20,19,13,15],3))