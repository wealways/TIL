import React,{ useState,useRef, useCallback } from 'react'
import TodoTemplate from './components/TodoTemplate'
import TodoInsert from './components/TodoInsert'
// import TodoList from './components/TodoList'
import TodoList2 from './components/TodoList2'

function createBulkTodos() {
  const array =[];
  for (let i =1; i<=2500; i++) {
    array.push({
      id:i,
      text:`할일 ${i}`,
      checked:false,
    });
  }
  return array
}

export default function App() {
  // 함수를 파라미터로 넘겨주는데 ()를 하면 리랜더링될 때 마다 호출되는데 이렇게 하면 
  // 처음 렌더링될 때만 실행된다.
  const [todos, setTodos] = useState(createBulkTodos)

  // 고윳값으로 사용될 id, ref를 사용하여 변수담기
  const nextId = useRef(2501)

  const onInsert = useCallback(text=>{
    const todo = {
      id:nextId.current,
      text:text,
      checked:false
    };
    setTodos(todos => todos.concat(todo));
    nextId.current += 1;
  },[todos])
  
  // 지우기 기능
  const onRemove = useCallback(id=>{
    setTodos(todos => todos.filter(todo=>todo.id!==id));
  },[todos])

  // 수정기능
  const onToggle = useCallback(id=>{
    setTodos(
      todos => 
      todos.map(todo=>
        todo.id===id ? {...todo,checked:!todo.checked} : todo
      ),
    );
  },[todos]);

  return (
    <div>
      <TodoTemplate>
        <TodoInsert onInsert={onInsert}/>
        {/* <TodoList todos={todos} onRemove={onRemove} onToggle={onToggle}/> */}
        <TodoList2 todos={todos} onRemove={onRemove} onToggle={onToggle}/>
      </TodoTemplate>
    </div>
  )
}
