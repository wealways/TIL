import React, { useState,useEffect } from 'react'
import styled from 'styled-components';
import NewsItem from './NewsItem';
import axios from 'axios';

const NewsListBlock = styled.div`
  box-sizing: border-box;
  padding-bottom: 3rem;
  width: 768px;
  margin: 0 auto;
  margin-top: 2rem;
  @media screen and (max-width:768px) {
    width: 100%;
    padding-left: 1rem;
    padding-right: 1rem;
  }
`;


function NewsList({category}) {

  const [articles,setArticles] = useState(null);
  const [loading,setLoading] = useState(false);

  useEffect(()=> {
    const fetchData = async () => {
      setLoading(true)
      try {
        const query = category === 'all' ? '' : `&category=${category}`
        const url =`https://newsapi.org/v2/top-headlines?country=kr${query}&apiKey=60eb5612ed934ea2a17296880ed4b6da`
        console.log(url)
        const res = await axios.get(url);
        setArticles(res.data.articles);

      } catch(e) {
        console.log('bad')
        console.log(e);
      }
      setLoading(false);
    };

    fetchData()
  },[category]);

  if (loading) {
    return <NewsListBlock> 대기중 ... </NewsListBlock>
  }
  if (!articles) {
    return null
  }

  return (
    <NewsListBlock>
      {articles.map(article=> (
        <NewsItem key={article.url} article={article} />
      ))}
    </NewsListBlock>
  )
}

export default NewsList
