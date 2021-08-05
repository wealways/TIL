import React from 'react'
import styled,{css} from 'styled-components'
/* 단순 변수의 형태가 아니라 여러 줄의 스타일 구문을 조건부로 설정해야 하는 경우에는 css를 불러와야 합니다. */

const sizes = {
  desktop:1024,
  tablet:768
}

const media = Object.keys(sizes).reduce((acc,label) => {
  acc[label] = (...args) => css`
  @media (max-width: ${sizes[label]/16}em) {
    ${css(...args)};
  }
  `;
  return acc;
},{});

const Box = styled.div`
// props로 넣어준 값을 직접 전달할 수 있습니다.
  background:${props => props.color || 'blue'};
  padding: 1rem;
  display:flex;
  width:1024px;
  margin: 0 auto;
  ${media.desktop`width:768px;`}
  ${media.tablet`width:100%;`};
`

const Button = styled.button`
  background: white;
  color:black;
  border-radius: 4px;
  padding:0.5rem;
  display:flex;
  align-items: center;
  justify-content: center;
  box-sizing:border-box;
  font-size:1rem;
  font-weight: 600;

  // Sass처럼 자기 자신 선택가능
  &:hover {
    background: rgba(255,255,255,0.9);
  }

  // inverted 값이 true일 때 특정 스타일을 부여할 수 있다.
  ${props=>
    props.inverted &&
    css`
      background: none;
      border: 2px solid white;
      color: white;
      &:hover {
        background: white;
        color: black;
      }
    `};
  & + button {
    margin-left:1rem;
  }
`;


export default function StyledComponent() {
  return (
    <Box color="black">
      <Button>안녕하세요</Button>
      <Button inverted={true}>테두리만</Button>
    </Box>
  )
}
