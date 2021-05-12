<template>
  <v-container>
    <home-banner/>
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
    }
  },
  components: {
    "gallery-row": GalleryRow,
    "home-banner": HomeBanner,
  },
};
</script>
