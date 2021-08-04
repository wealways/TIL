import React, {useState} from 'react'

export default function IterationSample() {
  const [names,setNames] = useState([
    {id:1,text:'눈사람'},
    {id:2,text:'눈'},
    {id:3,text:'얼음'}
  ])
  const [inputText, setInputText] = useState('')
  const [nextId,setNextId] = useState(4);

  const nameList = names.map(name=><li key={name.id} onDoubleClick={() => onRemove(name.id)}>{name.text}</li>)
  const onChange = (e) => {
    setInputText(e.target.value)
  } 
  const onClick = () => {
    const nextNames = names.concat({
      id:nextId,
      text:inputText
    })
    setNames(nextNames);
    setNextId(nextId+1);
    setInputText('');
  }
  const onRemove = (id) => {
    const nextNames = names.filter(name => name.id !== id);
    setNames(nextNames)
  }
  return (
    <>
      <input value={inputText} onChange={onChange} />
      <button onClick={onClick}>츄가</button>
      <ul>
        {nameList}
      </ul>
    </>
  )
}
