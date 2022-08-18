import React, { useState,useEffect } from 'react'

export default function Info() {

  const [name,setName] = useState('');
  const [nickname,setNickname] = useState('');
  // useEffect(()=> {
  //   console.log('랜더링이 완료되었습니다!');
  //   console.log({
  //     name,nickname
  //   });
  // },);
  // 처음 렌더링 될때만 실행하고 싶다면
  // useEffect(()=>{
  //   console.log('마운트될 때만 실행됩니다!!')
  // },[])
  // 특정값이 변경될 때마다 실행되고 싶다면!
  // useEffect(()=>{
  //   console.log('특정값이 변경되서 업데이트되는중!!')
  // },[name])
  // 뒷정리 하기 cleanup 기능
  useEffect(()=>{
    console.log('effect')
    return () => {
      console.log('cleanup')
    }
  },[])


  const onChangeName = (e) => {
    setName(e.target.value);
  }
  const onChangeNickname = (e) => {
    setNickname(e.target.value);
  }
  return (
    <div>
      <input
        name="name"
        placeholder="이름을 입력하세요."
        value={name}
        onChange={onChangeName}
      />
      <input
        name="nickname"
        placeholder="닉네임을 입력하세요."
        value={nickname}
        onChange={onChangeNickname}
      />
      <br/>
      <h2>이름 : {name}</h2>
      <h2>닉네임 : {nickname}</h2>
    </div>
  )
}
