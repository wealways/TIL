const sol = (str) => {
  // return Number(str.replace(/[^0-9]/g,''))
  let result = ''
  for (let s of str){
    if(!isNaN(s)) result+=s  
  }
  return parseInt(result)
}

console.log(sol('g0en2T0s8eSoft'))