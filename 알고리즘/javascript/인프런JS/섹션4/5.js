const sol = (k,cards) => {
  let answer
  let temp = new Set()
  for(let i=0;i<cards.length;i++){
    for(let j=i+1;j<cards.length;j++){
      for(let k=j+1;k<cards.length;k++){
        temp.add(cards[i]+cards[j]+cards[k])
      }
    }
  }
  return answer = Array.from(temp).sort((a,b)=>b-a)[k-1]
}

let arr=[13, 15, 34, 23, 45, 65, 33, 11, 26, 42];
console.log(sol(3, arr));