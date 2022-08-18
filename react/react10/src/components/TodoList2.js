// react-virtualized 를 활용하여 렌더링 최적화
import React, { useCallback } from 'react'
import { List } from 'react-virtualized'
import TodoListItem from './TodoListItem'
import './TodoList.scss'

function TodoList2({todos,onRemove,onToggle}) {
  const rowRenderer = useCallback(({index,key,style})=>{
    const todo = todos[index];
    return (
      <TodoListItem
        todo={todo}
        key={key}
        onRemove={onRemove}
        onToggle={onToggle}
        style={style}
      />
    );
  },[onRemove,onToggle,todos])
  
  return (
    <List
      className="TodoList"
      width={512}
      height={513}
      rowCount={todos.length}
      rowHeight={57}
      rowRenderer={rowRenderer}
      list={todos}
      style={{outline:'none'}}
    />
  );
};

export default React.memo(TodoList2);
