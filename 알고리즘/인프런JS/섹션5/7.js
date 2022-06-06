const sol = (str1,str2) => {

  let temp = new Map()
  for(let s of str1) {
    if(temp.has(s)) temp.set(s,temp.get(s)+1)
    else temp.set(s,1)
  }

  for(let s of str2){
    if(!temp.has(s) || temp.get(s)==0) return 'NO'
    temp.set(s,temp.get(s)-1);
  }
  return 'YES'
}

let a="AbaAeCe";
let b="baeeACA";
console.log(sol(a, b));