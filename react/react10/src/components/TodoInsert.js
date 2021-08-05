import React,{useState, useCallback} from 'react'
import {MdAdd} from 'react-icons/md'
import './TodoInsert.scss'

export default function TodoInsert({onInsert}) {
  const [value,setValue] = useState('')
  const onChange = useCallback(e=>{
    setValue(e.target.value);
  },[]);

  const onSubmet = useCallback((e)=>{
    onInsert(value);
    setValue('');

    //submit 이벤트는 브라우저에서 새로고침을 발생시킵니다.
    e.preventDefault();
  },[onInsert,value]);

  return (
    <div>
      <form
        className="TodoInsert"
        onSubmit={onSubmet}
      >
        <input
          placeholder="할 일을 입력하세요."
          value={value}
          onChange={onChange}
        />
        <button type="submit">
          <MdAdd />
        </button>
      </form>
    </div>
  )
}
