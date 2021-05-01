import React, {useState} from 'react';
import {ScrollView} from'react-native'
import styled from 'styled-components/native';

import Counter from './components/Counter';
import Form from './components/Form';
import Button from './components/Button';
import Length from './components/Length';
import Dog from './components/Dog';

const Container = styled.View`
  flex:1 ;
  background-color: #fff;
  justify-content:center;
  align-items: center;
`;

const App = () => {
  const [isVisible,setIsVisible] = useState(true);

  return (
    <ScrollView>
      <Container>
        <Dog />
        <Button
          title={isVisible ? 'Hide' : 'Show'}
          onPress={() => setIsVisible(prev => !prev)}
        />
        {/* 이거 무슨뜻 인지 모르겠음.. */}
        {isVisible && <Form />}
        <Counter />
        <Length/>
      </Container>
    </ScrollView>
  )
};

export default App;