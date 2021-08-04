import React,{useState} from 'react'

export default function EventPractice2() {
  
  const [username,setUsername] = useState('');
  const [message,setMessage] = useState('');

  const onChangeUsername = (e) => setUsername(e.target.value);
  const onChangeMessage = (e) => setMessage(e.target.value);
  const onClick = () => {
    alert(username + " : " + message)
    setUsername('')
    setMessage('')
  };
  const onKeyPress = (e) => {
    if(e.key==="Enter") onClick();
  };
  return (
    <div>
      <h1>이벤트 연습 - 함수형 컴포넌트</h1>
      <input 
        type="text"
        name="username"
        placeholder="이름"
        value={username}
        onChange={onChangeUsername}
      />
      <input 
        type="text"
        name="message"
        placeholder="아무거나 입력해주세여"
        value={message}
        onChange={onChangeMessage}
        onKeyPress={onKeyPress}
      />
      <button onClick={onClick}>확인</button>
    </div>
  )
}

