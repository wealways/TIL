import React from 'react'
import {
  MdCheckBoxOutlineBlank,
  MdCheckBox,
  MdRemoveCircleOutline,
} from 'react-icons/md'
import cn from 'classnames';
import './TodoListItem.scss'

function TodoListItem({todo,onRemove,onToggle, style}) {
  const {id,text,checked} = todo;

  return (
    <div className="TodoListItem-virtualized" style={style}>
      <div className="TodoListItem">
        <div className={cn('checkbox',{checked})} onClick={()=>onToggle(id)}>
          {checked ? <MdCheckBox/>: <MdCheckBoxOutlineBlank/>}
          <div className="text">{text}</div>
        </div>
        <div className="remove" onClick={()=>onRemove(id)}>
          <MdRemoveCircleOutline />
        </div>
        
      </div>
    </div>
  )
};

// React.memo() 안에 넣어주면, 상태가 변하는 것만 rerendering을 하게 됩니다.
export default React.memo(TodoListItem) 