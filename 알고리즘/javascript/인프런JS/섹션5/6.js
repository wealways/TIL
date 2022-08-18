const sol = (str) => {
  let answer 
  let temp = new Map()
  for(let s of str) {
    if(temp.has(s)) temp.set(s,temp.get(s)+1)
    else temp.set(s,1)
  }
  let maxV = Number.MIN_SAFE_INTEGER
  for(let[key,val] of temp){
    if(val>maxV) {
      maxV = val;
      answer =key

    }
  }
  return answer
}

console.log(sol('BACBACCACCBDEDE'))