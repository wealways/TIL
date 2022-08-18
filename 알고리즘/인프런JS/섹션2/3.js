const game = (a,b) =>{
    let result =''
    switch (a) {
        case 1:
            if(b==1){
                result = 'D'
            }else if(b==2){
                result = 'B'
            }else result ='A'
            break;
        case 2:
            if(b==1){
                result = 'A'
            }else if(b==2){
                result = 'D'
            }else result ='B'
            break;
        case 3:
            if(b==1){
                result = 'B'
            }else if(b==2){
                result = 'A'
            }else result ='D'
            break;
    }
    return result
}
const sol = (N,As, Bs) => {
    for(i=0;i<N;i++){
        console.log(game(As[i],Bs[i]))
    }
}

sol(5,[2,3,3,1,3],[1,1,2,2,3])