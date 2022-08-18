import React, {useState, useRef, useCallback} from 'react'
import TodoTemplate from './components/TodoTemplate'
import TodoInsert from './components/TodoInsert'
import TodoList from './components/TodoList'

function createDummyTodos() {
  const array = []
  for (let i = 1; i<=2500;i++) {
    array.push({
      id:i,
      text:`할일 ${i}`,
      checked: i%3 === 0 ? true : false
    });
  }
  return array
}

function App() {
  const [todos,setTodos] = useState(createDummyTodos)
  const nextId = useRef(2501);

  const onInsert = useCallback(text => {
    const todo = {
      id:nextId.current,
      text:text,
      checked: false
    };
    setTodos(todos => todos.concat(todo));
    nextId.current += 1;
  },[todos])

  const onRemove = useCallback(id=> {
    setTodos(todos => todos.filter(todo => todo.id !==id));
  },[todos])

  const onToggle = useCallback(id=>{
    setTodos(todos => todos.map(todo => todo.id===id ? {...todo,checked:!todo.checked} : todo ))
  },[todos])

  return (
    <div>
      <TodoTemplate>
        <TodoInsert onInsert={onInsert}/>
        <TodoList todos={todos} onRemove={onRemove} onToggle={onToggle}/>
      </TodoTemplate>
    </div>
  )
}

export default App
