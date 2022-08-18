ES6의 비구조화 할당 문법

- 배열 비구조화 할당

```react
const array=[1,2]
const one = array[0];
const two = array[1];

// 위에거 너무 비효율적
const array= [1,2]
const [one,two] = array
```



클래스형 컴포넌트를 만들때 `this.setState`를 사용하여 state 값을 업데이트할 때는 비동기적으로 동작합니다. 따라서, 함수를 인자로 넣어줌으로써 해결할 수 있습니다.

```react
// 아래 예시에서 onClick 이벤트가 발생해도 number의 숫자는 1만 증가한다.
onClick={()=>{
    this.setState({number: number+1});
    this.setState({number: this.state.number + 1});
}}

// 그러나 다음과 같이 함수를 this.setState의 인자로 넣어주면 해결 가능하다.
onClick={()=>{
    this.setState(prevState=>{
        return {
            number: prevState + 1
        }
    })
}}
```

`this.setState` 의 두번째 파라미터로 콜백함수를 등록할 수 있다.

---

배열이나 객체를 `setState` 또는 `useState` 를 통해 업데이트해야할 때는

⭐배열이나 객체 사본을 만들고 그 사본에 값을 업데이트한 후, 그 사본의 상태를 setState 혹은 세터함수를 통해 업데이트해야합니다.



---

이벤트 이름은 카멜포기법을 사용합니다.

이벤트에 실행할 자바스크립트 코드를 전달하는 것이 나리ㅏ, 함수 형태의 값을 전달합니다.

---

## ref

언제사용할까? DOM을 직접적으로 건드려야 할 때

