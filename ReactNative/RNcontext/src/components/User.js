// src/components/User

import React,{useContext} from 'react';
import styled from 'styled-components/native';
// import {UserConsumer} from '../contexts/User';
import UserContext from '../contexts/User';

const StyledText = styled.Text`
  font-size:24px;
  margin:10px;
`;

const User = () => {
  const {user} = useContext(UserContext);

  return(
    // <UserConsumer>
    //   {({user}) => <StyledText>Name: {user.name}</StyledText>}
    // </UserConsumer>
    <StyledText>Name:{user.name}</StyledText>
  );
};

export default User;