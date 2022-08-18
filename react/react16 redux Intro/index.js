import { createStore } from "redux";

const divToggle = document.querySelector('.toggle');
const counter = document.querySelector('h1');
const btnIncrease = document.querySelector('#increase');
const btnDecrease = document.querySelector('#decrease');


// 액션 타입과 액션 생성 함수 정의
const TOGGLE_SWITCH = 'TOGGLE_SWITCH';
const INCREASE = 'INCREASE';
const DECREASE = 'DECREASE';

const toggleSwitch = () => ({type: TOGGLE_SWITCH })
const increase = difference => ({type:INCREASE,difference});
const decrese = () => ({type:DECREASE});

// 초기값 설정
const initialState = {
  toggle:false,
  counter:0
};

//리듀서는 변화를 일으키는 함수입니다. 파라미터로는 state와 action 값을 받아옵니다.
function reducer(state=initialState,action) {
  switch(action.type) {
    case TOGGLE_SWITCH:
      return {
        ...state,
        toggle: !state.toggle
      };
    case INCREASE:
      return {
        ...state,
        counter: state.counter + action.difference
      };
    case DECREASE:
      return {
        ...state,
        counter:state.counter -1
      };
    default:
      return state;
  }
}

// 스토어 만들기
const store = createStore(reducer);

const render = () => {
  const state= store.getState(); // 현재 상태를 불러옵니다.

  // 토글 처리
  if(state.toggle) {
    divToggle.classList.add('active')
  } else {
    divToggle.classList.remove('active')
  }

  counter.innerText = state.counter;
};

render();

// 구독하기
store.subscribe(render);


//액션 발생시키기
divToggle.onClick = () => {
  store.dispatch(toggleSwitch());
};

btnIncrease.onClick = () => {
  store.dispatch(increase(1))
};

btnDecrease.onClick = () => {
  store.dispatch(decrese())
};
