const isPrime = (num) => {
  if(num==1) return false
  console.log(parseInt(Math.sqrt(num)))
  for(let i=2;i<=parseInt(Math.sqrt(num));i++){
    if(num%i==0) return false
  }
  return true
}

const sol = (arr) => {
  let answer = []
  for(let a of arr) {
    a = a.toString().split('').reverse().join('')
    if(isPrime(parseInt(a))){
      answer.push(parseInt(a))
    }
  }
  return answer
}

console.log(sol([32,55,62,20,250,370,200,30,100]))
