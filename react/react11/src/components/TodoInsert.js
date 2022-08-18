import React, {useState,useCallback} from 'react'
import {MdAdd} from 'react-icons/md'
import './TodoInsert.scss'

function TodoInsert({onInsert}) {
  const [value,setValue] = useState('')
  
  const onChange = useCallback(e => {
    setValue(e.target.value)
  },[]);

  const onSubmit = useCallback(e => {
    onInsert(value);
    setValue('');

    e.preventDefault();
  },[onInsert,value])

  return (
    <div>
      <form className="TodoInsert" onSubmit={onSubmit}>
        <input placeholder="할 일을 입력하세요." value={value} onChange={onChange}/>
        <button type="submit">
          <MdAdd/>
        </button>
      </form>
    </div>
  )
}

export default TodoInsert
