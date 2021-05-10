<template>
  <v-container>
    <home-banner
      :img_src="banner_img_src"
      :title="banner_title"
      :desc="banner_desc"
    />
    <gallery-row :header="header"></gallery-row>
    <gallery-row :header="header2"></gallery-row>
    <p>{{ computedArticles }}</p> 
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
      /*Banner Fields*/
      banner_img_src:
        "https://i0.wp.com/johnnyalucard.com/wp-content/uploads/2020/04/shrek.jpg",
      banner_title: "Top story",
      banner_desc: "hahahah",

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
