<template>
  <v-container>
    <home-banner :article="bannerArticle[0]" :path="bannerArticle[1]"/>
    <gallery-row v-for="(item, index) in computedArticles" :key="index" :header="index"></gallery-row>
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
      console.log("in Home computed:", store.state.articles)
      if (store.state.articles) {
        return store.state.articles
      } else {
        return "loading..."
      }
    },
    // randomOutlet: function(){
    //   return Object.keys(store.state.articles)[Math.floor(Math.random() * Object.keys(store.state.articles).length)]
    // },
    // randomIndex: function(){
    //   return Math.floor(Math.random() * store.state.articles[randomOutlet].length)
    // },
    bannerArticle: function(){
      console.log("in Home Banner computed:", store.state.articles)
      if (store.state.articles && Object.keys(store.state.articles).length > 0) {
        let randomOutlet = Object.keys(store.state.articles)[Math.floor(Math.random() * Object.keys(store.state.articles).length)]
        let randomIndex = Math.floor(Math.random() * store.state.articles[randomOutlet].length)
        return [store.state.articles[randomOutlet][randomIndex], `/${randomOutlet}/${randomIndex}`]
      } else {
        return [{title:"loading...", description:"loading...", urlToImage:"loading..."}, ""]
      }
    }
  },
  components: {
    "gallery-row": GalleryRow,
    "home-banner": HomeBanner,
  },
};
</script>
