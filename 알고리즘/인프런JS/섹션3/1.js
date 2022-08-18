const sol = (str) => {
  let a = str.split('').map(a=>a.toUpperCase()).reverse().join('')
  let b = str.split('').map(a=>a.toUpperCase()).join('') 
  if(a==b) return 'YES'
  else return 'NO'
}

console.log(sol('gooG'))
console.log(sol('gog'))
console.log(sol('goD'))