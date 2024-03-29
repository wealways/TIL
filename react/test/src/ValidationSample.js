import React, { Component } from 'react'
import './ValidationSample.css';

export default class ValidationSample extends Component {
  state = {
    password:'',
    clicked:false,
    validated:false
  }
  handleChange = (e) => {
    this.setState({
      password: e.target.value
    })
  }
  handleButtonClick = () =>{
    this.setState({
      clicked:true,
      validated:this.state.password === '0000'
    });
    this.input.focus();
  }
  render() {
    return (
      <div>
        <input 
          type="password"
          value={this.state.password}
          ref={(ref)=>this.input=ref}
          onChange={this.handleChange}
          className={this.state.clicked ? (this.state.validated ? 'success' : 'failure') : ''}
        />
        <button onClick={this.handleButtonClick}>확인하기</button>
      </div>
    )
  }
}
