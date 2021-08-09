import React from 'react'

const data ={
  velopert:{
    name:'김민주',
    description: '리액트를 좋아하는 개발자'
  },
  gildong:{
    name:'hong',
    description:'hi my name is hong'
  }
};

function Profile({match}) {
  const {username} = match.params;
  const profile = data[username]
  if(!profile) {
    return <div>존재하지 않는 사용자입니다.</div>
  }
  return (
    <div>
      <h3>
        {username}({profile.name})
      </h3>
      <p>{profile.description}</p>
    </div>
  );
};

export default Profile
