<template>
  <div>
    <h2>로또번호 추천</h2>
    <button @click="getLuckyNums">Pick My Lotto Numbers</button>
    <h2>로또 번호 {{ $route.params.lottoNum }}개 추천</h2>
    <p>오늘의 추천 로또 번호</p>
    <p>{{ selectedLuckyNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLotto',
  data: function() {
    return {
      sampleNums: [],
      selectedLuckyNums: [],
    }
  },
  methods: {
    getLuckyNums() {
      const numbers = _.range(1,46)
      this.sampleNums = _.sampleSize(numbers,this.$route.params.lottoNum)
      // this.sampleNums = _.sampleSize(numbers,6)

      this.selectedLuckyNums = _.sortBy(this.sampleNums)
      // this.$router.push({ name: 'Result' })
    },
  }
}
</script>

<style>

</style>