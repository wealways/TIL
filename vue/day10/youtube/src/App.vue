<template>
  <div id="app">
    <header>
      <h1>youtube</h1>
      <SearchBar @searched-videos="searchedVideos"/>
    </header>
    <section>
      <VideoDetail v-if="isVideoSelected" :video="selectedVideo"/>
      <VideoList :videoList="videoList" @select-video="selectVideo"/>
    </section>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'


export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      videoList:[],
      selectedVideo: {},
      isVideoSelected:false,
    }
  },
  methods: {
    searchedVideos(videoList) {
      this.videoList = videoList
    },
    selectVideo(video){
      console.log('select비디오 호출!')
      console.log(video)
      this.selectedVideo = video
      this.isVideoSelected = true
    },
  }
}
</script>

<style>
header,section {
  width: 80%;
  margin: 0 auto;
  padding: 1rem 0;
}
section {
  display:flex;
}
</style>
