<template>
  <v-container>
      <v-row class="banner-container" 
      @click="goArticle">
        <v-col lg="8" md="8" sm="8" class="pa-0">
          <v-parallax
          :src="computedArticles.urlToImage"
          height=500
          >
          </v-parallax>
        </v-col>
        <v-col lg="4" md="4" sm="4">
            <h1 class="banner-text">
               {{ computedArticles.title }}
            </h1>
            <br/>
            <p class="banner-text">
               {{ computedArticles.description }}
            </p>
        </v-col>
      </v-row>
  </v-container>
</template>

<style>
.banner-container{
  background: #000000;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  size: cover;
}

.banner-text{
  color: #FFFFFF;
  font: Dubai;
}
</style>

<script>
import {store} from "../store.js";

  export default {
    name: 'HomeBanner',
    data: () => ({
    }),
    computed: {
      computedArticles: function(){
        console.log("in Home Banner computed:", store.state.articles)
        if (store.state.articles && store.state.articles.length>0)
          return store.state.articles[Math.floor(Math.random() * store.state.articles.length)];
        return "loading..."
      }
    },
    methods: {
      goArticle() {
        this.$router.push({ path: `/article/${this.computedArticles.id-1}` }) 
      },
    },
  }
</script>

