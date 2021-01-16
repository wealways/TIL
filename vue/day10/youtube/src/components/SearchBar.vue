<template>
  <div>
    <input class="searchBar" type="text" @keypress.enter="searchVideo">
  </div>
</template>

<script>
import axios from 'axios'

const BASE_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'SearchBar',
  data() {
    return {
      userInput:'',
    }
  },
  methods:{
    searchVideo(e) {
      this.userInput = e.target.value

      const config = {
        params: {
          part: 'snippet',
          key: API_KEY,
          q: this.userInput
        }
      }
      axios.get(BASE_URL,config)
      .then(res=>{
        console.log('데이터 보낼게!')
        this.$emit('searched-videos',res.data.items)
      })
      .catch(err=>{
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
  .searchBar {
    width: 100%;
    padding: 0.5rem;
    font-size: 1.25rem;
  }
</style>