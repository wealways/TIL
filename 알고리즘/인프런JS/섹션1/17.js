const sol = (arr) => {
    let result = []
    for(let a of arr){
        if(!result.includes(a)){
            console.log(a)
            result.push(a)
        }
    }
}

sol(['good','time','good','time','student'])