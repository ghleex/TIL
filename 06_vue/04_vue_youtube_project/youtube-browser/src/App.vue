<template>
  <div id="app">
    <!-- 만약 inputChange 이벤트가 일어나면 onInputChange 라는 메소드 실행 -->
    <search-bar @inputChange="onInputChange"></search-bar>
    <!-- 왼쪽의 videos 는 VideoList.vue 의 props 에서 받을 변수, -->
    <!-- 오른쪽의 videos 는 videos 배열 -->
    <div class="row">
      <video-detail :video="selectedVideo"></video-detail>
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
    </div>
  </div>
</template>

<script>
import axios from "axios"; // 외부에서 설치한 것이므로 경로 생략 가능
import SearchBar from "./components/SearchBar";
import VideoList from "./components/VideoList";
import VideoDetail from "./components/VideoDetail";
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
const API_URL = "https://www.googleapis.com/youtube/v3/search";

export default {
  name: "App", // 최상단 컴포넌트에는 이름이 없어도 되지만, 명시적으로 작성.
  data() {
    return {
      // component 에서 데이터 리턴 시 객체(object)로 한 번 더 감싸주어야 데이터 반환 가능
      // namespace 때문
      videos: [],
      selectedVideo: null
    };
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail
  },
  methods: {
    onVideoSelect(video) {
      this.selectedVideo = video;
    },
    onInputChange(inputValue) {
      axios
        .get(API_URL, {
          params: {
            key: API_KEY,
            type: "video",
            part: "snippet",
            q: inputValue
          }
        })
        .then(response => {
          // 함수 내 함수 이므로 반드시 Arrow Function 을 사용해야 함
          this.videos = response.data.items;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style>
</style>
