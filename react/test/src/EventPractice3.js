import React,{useState} from 'react'

function EventPractice3() {
  const [form,setForm] = useState({
    username:'',
    message:''
  })
  const {username,message} = form
  const onChange = (e) =>{
    const nextForm = {
      ...form,
      [e.target.name]:e.target.value
    };
    setForm(nextForm)
  }
  const onClick = () => {
    alert(username + ': ' + message)
    setForm({
      username:'',
      message:''
    })

  }
  const onKeyPress = (e) => {
    if(e.key==="Enter") onClick();
  }

  return (
    <div>
      <h1>이벤트 연습 - 함수현 컴포넌트 간편화</h1>
      <input
        type="text"
        name="username"
        placeholder="이름"
        value={username}
        onChange={onChange}
      />
      <input
        type="text"
        name="message"
        placeholder="아무거나입력"
        value={message}
        onChange={onChange}
        onKeyPress={onKeyPress}
      />
      <button onClick={onClick}>확인</button>
    </div>
  )
}

export default EventPractice3
