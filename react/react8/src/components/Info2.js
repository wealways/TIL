import React, {useReducer} from 'react'

function reducer(state,action) {
  return {
    ...state,
    [action.name]:action.value
  };
}

export default function Info2() {
  const [state,dispatch] = useReducer(reducer,{
    name:'',
    nickname:''
  });
  const {name,nickname} = state;
  const onChange = (e) => {
    dispatch(e.target);
  }

  return (
    <div>
      <div>
        <input
         name="name"
         value={name}
         onChange={onChange}
        />
        <input
         name="nickname"
         value={nickname}
         onChange={onChange}
        />
      </div>
      <div>
        <h2>이름: {name}</h2>
        <h2>별명: {nickname}</h2>
      </div>
      
    </div>
  )
}
