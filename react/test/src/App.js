import './App.css';
// import MyComponent from './MyComponent';
// import Counter from './Counter';
// import Say from './Say';
// import EventPractice from './EventPractice';
// import EventPractice2 from './EventPractice2';
// import EventPractice3 from './EventPractice3';
// import ValidationSample from './ValidationSample';
import React,{Component} from 'react';
import ScrollBox from './ScrollBox';

// function App() {
//   // return <MyComponent name="react" favoriteNumber={1}> 리액트 </MyComponent>;
//   // return <Counter/>
//   // return <Say />
//   // return <EventPractice />
//   // return <EventPractice2 />
//   // return <EventPractice3 />
//   // return <ValidationSample />
  
// };

class App extends Component {
  render() {
    return (
      <div>
        <ScrollBox ref={(ref) => this.scrollBox=ref}/>
        <button onClick={()=>this.scrollBox.scrollToBottom()}>
          맨 밑으로
        </button>
      </div>
    )
  }
}

export default App;
