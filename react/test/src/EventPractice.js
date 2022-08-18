import React, { Component } from 'react'

export default class EventPractice extends Component {

  state = {
    username:'',
    message:''
  }

  // 메서드 바인딩을 통한 편리화
  // constructor(props){
  //   super(props)
  //   this.handleChange = this.handleChange.bind(this);
  //   this.handleClick = this.handleClick.bind(this);
  // }

  // handleChange(e) {
  //   this.setState({
  //     message:e.target.value
  //   })
  // };

  // handleClick(e) {
  //   alert(this.state.message)
  //   this.setState({
  //     message:''
  //   })
  // };
  // =======================================

  // 바벨의 transform-class-properties
  handleChange = (e) => {
    this.setState({
      [e.target.name] : e.target.value
    })
  };
  handleClick = (e) => {
    alert(this.state.username + ' : ' + this.state.message)
    this.setState({
      username:'',
      message:''
    })
  };
  handleKeyPress = (e) => {
    if(e.key==='Enter') {
      this.handleClick();
    }
  }
  render() {
    return (
      <div>
        <h1>이벤트 연습</h1>
        <input
          type="text"
          name="username"
          placeholder="이름을 입력하세요"
          value={this.state.username}
          onChange={this.handleChange}
        />
        <input
          type="text"
          name="message"
          placeholder="아무거나 입력"
          value={this.state.message}
          onChange={this.handleChange}
          onKeyPress={this.handleKeyPress}
        />
        <button
          onClick={this.handleClick}
        >확인</button>
      </div>
    )
  }
}
