<template>
  <v-container>
    <home-banner :article="bannerProps.article" :path="bannerProps.path"/>
    <gallery-row v-for="(item, index) in computedArticles" :key="index" :header="index" :articles="item"></gallery-row>
  </v-container>
</template>

<script>
import GalleryRow from "../components/GalleryRow";
import HomeBanner from "../components/HomeBanner";
import {store} from "../store.js";

export default {
  name: "Home",
  computed:{
    computedArticles: function(){
      console.log("computedArticles", store.state.articles)
      if (store.state.articles) {
        return store.state.articles
      } else {
        return "loading..."
      }
    },
    bannerProps: function(){
      if (store.state.articles && Object.keys(store.state.articles).length > 0) {
        let randomOutlet = Object.keys(store.state.articles)[Math.floor(Math.random() * Object.keys(store.state.articles).length)]
        let randomIndex = Math.floor(Math.random() * store.state.articles[randomOutlet].length)
        return {article: store.state.articles[randomOutlet][randomIndex], path: `/${randomOutlet}/${randomIndex}`}
      } else {
        return {article: {title:"loading...", description:"loading...", urlToImage:"loading..."}, path: ""}
      }
    }
  },
  components: {
    "gallery-row": GalleryRow,
    "home-banner": HomeBanner,
  },
};
</script>
