const sol = (str) => {
  let answer = ''
  let cnt = 1
  for(let i=0;i<str.length;i++){
    if(answer.at(-1)==str[i]){
      cnt+=1
    }else{
      if(cnt==1) {
        answer +=str[i]
      }
      else {
        answer +=cnt
        answer += str[i]
        cnt=1
      }
    }
  }
  return answer
}

console.log(sol('KKHSSSSSSSE'))