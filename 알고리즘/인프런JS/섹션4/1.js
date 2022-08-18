const sol = (arr) => {
  let maxV = Number.MIN_SAFE_INTEGER
  let ans = 0
  for(let a of arr){
    // a = String(a)
    let v = a.toString().split('').reduce((arr,c)=>arr+parseInt(c),0)
    if(maxV<=v){
      maxV = v
      ans = a
    }
  }
  return ans
}

console.log(sol([128,460,603,40,521,137,123]))