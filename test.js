//Promise 객체 만들기

function increase(num) {
  const promise = new Promise((resolve,reject) => {

    setTimeout(()=>{
      const result = num + 10
      if(result >50) {
        const e = new Error('50보다 커!!')
        return reject(e)
      }
      resolve(result)
    },1000);
  });
  return promise
}

increase(0)
  .then(num=>{
    console.log(num)
    return increase(num)
  })
  .then(num=>{
    console.log(num)
    return increase(num)
  })
  .then(num=>{
    console.log(num)
    return increase(num)
  })
  .then(num=>{
    console.log(num)
    return increase(num)
  })
  .then(num=>{
    console.log(num)
    return increase(num)
  })
  .then(num=>{
    console.log(num)
    return increase(num)
  })
  .catch(e=>{
    console.log(e)
  })