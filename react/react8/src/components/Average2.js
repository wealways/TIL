import React,{useState,useMemo,useCallback, useRef} from 'react'

const getAverage = (nums) => {
  console.log('평균 계산중...')
  if(nums.length===0) return 0;
  const sum = nums.reduce((a,b) => a+b);
  return sum/nums.length
}

export default function Average2() {
  const [list,setList] = useState([])
  const [num,setNum] = useState('');
  const inputEl = useRef(null);

  const onChange = useCallback((e)=>{
    setNum(e.target.value);
  },[]);
  const onInsert = useCallback((e)=>{
    const nextList = list.concat(parseInt(num));
    setList(nextList);
    setNum('');
    inputEl.current.focus();
  },[list,num]); // list또는 num이 바뀔 때만 사용
  const avg = useMemo(()=>getAverage(list),[list])
  return (
    <div>
      <input value={num} onChange={onChange} ref={inputEl} />
      <button onClick={onInsert}>등록</button>
      <ul>
        {list.map((val,idx)=>(
          <li key={idx}>{val}</li>
        ))}
      </ul>
      <div>
        평균값: {avg}
      </div>
    </div>
  )
}
