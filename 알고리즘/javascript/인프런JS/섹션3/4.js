function solution(s, t){
  let answer=[];
  let p=1000;
  for(let x of s){
      if(x===t){
          p=0;
          answer.push(p);
      }
      else{
          p++;
          answer.push(p);
      }
  }
  p=1000;
  for(let i=s.length-1; i>=0; i--){
      if(s[i]===t) p=0;
      else{
          p++;
          answer[i]=Math.min(answer[i], p);
      }
  }
  return answer;
}

let str="teachermode";
console.log(solution(str, 'e'));

const sol = (str,target) => {
    let answer = []
    let n =Number.MAX_SAFE_INTEGER
    for(let s of str) {
        if(s!=target){
            n+=1
        }else{
            n = 0
        }
        answer.push(n)
    }

    n = Number.MAX_SAFE_INTEGER
    for(let i = str.length-1;i>=0;i--){
        if(str[i]!=target){
            n+=1
        }
        else{
            n=0
        }
        
        if(answer[i]>=n){
            answer[i]=n
        }
    }
    return answer
}
console.log(sol(str, 'e'));