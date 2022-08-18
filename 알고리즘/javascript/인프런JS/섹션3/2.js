const checkChar = (a) => {
  let n = a.charCodeAt() 
  if((n>=65 && n<=90) || (n>=97 && n<=122)) return a
  
}

const sol = (str) => {
  // const UpperStr = str.toUpperCase()
  // const fixedStr = UpperStr.split('').filter(s=>checkChar(s))
  const fixedStr = str.toUpperCase().replace(/[^A-Z]/g,'')
  console.log(fixedStr)
  const len = fixedStr.length
  
  for(let i=0;i<Math.floor(len/2);i++){
    if(fixedStr[i]!=fixedStr[len-1-i]) return 'NO'
  }
  return 'YES'

}

console.log(sol("found7, time: study; Yduts; emit, 7Dnuof"))