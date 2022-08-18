const sol = (arr) => {
  let result =[]
  for(let a of arr){
    let point = 1
    for(let b of arr){
      if(a<b) point += 1
    }
    result.push(point)
  }
  return result 
}

console.log(sol([87,89,92,100,76]))
console.log(sol([92,92,92,80]))
