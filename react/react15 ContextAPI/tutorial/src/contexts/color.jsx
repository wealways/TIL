import React, {createContext,useState} from 'react';

// context 정의하기. 현재 상태와 액션 정의
const ColorContext = createContext({
  state:{color:'black', subcolor:'red'},
  actions:{
    setColor: () => {},
    setSubcolor: () => {}
  }
});

//
const ColorProvider = ({children}) => {
  const [color,setColor] = useState('black');
  const [subcolor,setSubcolor] = useState('red');

  const value = {
    state:{color,subcolor},
    actions: {setColor,setSubcolor}
  };
  return (
    <ColorContext.Provider value={value}>{children}</ColorContext.Provider>
  );
};

//  const ColorConsumer = ColorContext.Consumer 이것과 같은 의미
const {Consumer:ColorConsumer} = ColorContext


export {ColorProvider,ColorConsumer};

export default ColorContext;