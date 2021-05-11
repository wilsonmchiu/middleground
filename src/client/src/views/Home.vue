<template>
  <v-container>
    <home-banner/>
    <gallery-row :header="header"></gallery-row>
    <gallery-row :header="header2"></gallery-row>
  </v-container>
</template>

<script>
import GalleryRow from "../components/GalleryRow";
import HomeBanner from "../components/HomeBanner";
import {store} from "../store.js";

export default {
  name: "Home",

  data() { 
    return {
      /*Gallery Row Fields Start*/
      header: "Header 1",
      header2: "Header 2",
    }
  },
  computed:{
    computedArticles: function(){
      console.log("in Home computed:", store.state.articles)
      if (store.state.articles && store.state.articles.length>0)
        return store.state.articles
      return "loading..."
    }
  },
  components: {
    "gallery-row": GalleryRow,
    "home-banner": HomeBanner,
  },
  methods: {
    
  },

};
</script>
