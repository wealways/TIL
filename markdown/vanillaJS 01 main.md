# Vanilla JS 로 컴포넌트 만들기 1 - 컴포넌트와 상태관리

프로그래머스 개발 과제를 수행하려면, Vue React 뿐만 아니라 axios lodash 그 어떤 것도 쓰면 안되는데, 컴포넌트, 형상관리를 JS로 하는 방법을 정확하게 숙지하고 있지 못했습니다.

그래서 이번 기회에 제대로 배워보고자 합니다.

## 🔵 컴포넌트와 상태관리

### 상태관리의 탄생

브라우저와 JavaScript가 발전하는 과정에서 아예 브라우저(클라이언트)단에서 렌더링을 하고, 서버에서는 `REST API` 혹은 `GraphQL` 같이 브라우저 렌더링에 필요한 데이터만 제공하는 형태로 기술이 발전해왔습니다. 

`DOM`을 다루는 행위는 급격하게 감소했고, `**상태(State)**`를 기준으로 `DOM`을 렌더링하는 형태로 발전을 하게 되었다는 의미입니다. 

이러한 과정 속에서 `Client-Side-Rendering`이라는 개념과 `상태관리`라는 개념이 생겨나게 됩니다.

> **SSR 그리고 CSR**
>
> SSR (Server-Side-Rendering)
>
> - 서버에서 HTML을 만들어서 클라이언트에 넘겨줍ㄴ디ㅏ.
> - 따라서 클라이언트(브라우저)에서는 굳이 데이터를 깊은 단계까지, 정교하게 관리할 필요가 없었다.
>
> CSR(Client-Side-Rendering)
>
> - JS가 발전하면서 아예 클라이언트(브라우저)에서 모든 렌더링을 처리하려는 시도가 계속 되었고, 이에 따라 `React`,`Angular`, `Vue` 같은 프레임워크(라이브러리)가 탄생하였습니다.
> - 브라우저에서 렌더링을 하기 위해선, 렌더링에 필요한 상태를 정교하게 관리해야 했습니다.
> - 그래서 `Redux`, `Vuex` 같은 상태관리 라이브러리(프레임워크)가 생겨났습니다.

[네이버 FE2019 - 데이터 상태관리, 그것을 알려주마](https://www.youtube.com/watch?v=o4meZ7MRd5o&ab_channel=naverd2)

### 컴포넌트

`Angular`가 `CSR`의 시작이었다면, `React`는 `컴포넌트 기반 개발`의 시작이었고, `Vue`는 두개의 장점을 모두 수용한 것입니다.

어쨌든 중요한 점은 **현 시점의 웹 어플리케이션은 컴포넌트 단위로 설계되고 개발된다**는 것이다. 그리고 컴포넌트마다 컴포넌트를 렌더링할 때 필요한 상태를 관리하게 되었으며, `Proxy` 혹은 `Observer Pattern` 등을 이용하여 이를 구현한다.