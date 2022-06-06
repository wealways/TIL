const sol = (arr,target) => {
  let answer 
  arr.sort((a,b)=>(a[0]+a[1]-(b[0]+b[1])))
  for(let i=0;i<arr.length;i++){
    let price = Number.MIN_SAFE_INTEGER
    let temp = [0,0]
    let sumV = 0
    for(let j=0;j<arr.length;j++){
      let tempSumV = temp[0]
      if(i==j){
        tempSumV= sumV + arr[j][0] /2
      }else{
        tempSumV= sumV + arr[j][0]
      }
      tempSumV = sumV + arr[j][1]
      if(tempSumV<=target){
        sumV = tempSumV
        temp[0]=sumV
        temp[1]+=1
      }else{
        break
      }
    }
    console.log(temp)
    console.log(answer)
    console.log('---')
    if(price<=temp[0]) answer=temp
  }
  return answer
} 

let arr=[[6, 6], [2, 2], [4, 3], [4, 5], [10, 3]];
console.log(sol(arr,28));