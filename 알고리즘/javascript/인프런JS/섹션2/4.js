const sol = (arr) => {
  let result = 0
  let point = 1
  arr.forEach(a=>{
    if(a){
      result += point
      point +=1
    }else{
      point = 1
    }
  })
  return result
}

console.log(sol([1,0,1,1,1,0,0,1,1,0]))