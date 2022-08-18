import React, {createContext, useState} from 'react'

//  consumer가 있는 컨텍스트 정의하기
const ColorContext = createContext({
  state:{color:'black',subcolor:'red'},
  actions:{
    setColor: () => {},
    setSubcolor: () => {},
  }
})

//프로바이더.. 제공하는 얘들인데 children 넘겨줘야합니다
// 프로바이더는 value가 무조건 필요합니다.
const ColorProvider = ({children}) => {
  const [color,setColor] = useState('black');
  const [subcolor,setSubcolor] = useState('red');

  const value = {
    state:{color,subcolor},
    actions:{setColor,setSubcolor}
  }

  return (
    <ColorContext.Provider value={value}>{children}</ColorContext.Provider>
  )
};

// 나는 provider하고 consumer만 넘겨줄거에요. 
const {Consumer:ColorConsumer} = ColorContext

export {ColorProvider,ColorConsumer};
export default ColorContext;