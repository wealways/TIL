<template>
  <div class="videoList">
    <VideoListItem
      v-for="video in videoList"
      :key="video.etag"
      :video="video"
      @select-video="selectVideo"
    />
    <!-- <div
    v-for="video in videoList"
    :key="video.etag"
    class="videoListItem"
    >
      <img width=360 :src="thumbnailUrl(video)" alt="">
      <div>
        <div class="videoListItem__title">{{video.snippet.title | unescape}}</div>
        <div class="videoListItem__channelTitle">{{video.snippet.channelTitle}}</div>
        <div class="videoListItem__description">{{video.snippet.description}}</div>
      </div>
    </div> -->
  </div>
</template>

<script>
// import _ from 'lodash'
import VideoListItem from '@/components/VideoListItem'

export default {
  name:'VideoList',
  components: {
    VideoListItem
  },
  props: {
    videoList: Array,
  },
  methods: {
    // thumbnailUrl(video) {
    //   return video.snippet.thumbnails.high.url
    // },
    selectVideo(video) {
      this.$emit('select-video',video)
    }
  },
  // filters: {
  //   unescape(value) {
  //     return _.unescape(value)
  //   }
  // },
}
</script>

<style>
.videoList {
  width: 30%;
}
/* .videoListItem {
  display:flex;
}
.videoListItem__title {
  font-size:1.25rem;
  font-weight:bold;
} */
</style>