<template>
  <v-container>
      <v-row class="banner-container" 
      @click="goArticle">
        <v-col lg="8" md="8" sm="8" class="pa-0">
          <v-parallax
          :src="computedArticles[randomOutlet][0].urlToImage"
          height=500
          >
          </v-parallax>
        </v-col>
        <v-col lg="4" md="4" sm="4">
            <h1 class="banner-text">
               {{ computedArticles[randomOutlet][0].title }}
            </h1>
            <br/>
            <p class="banner-text">
               {{ computedArticles[randomOutlet][0].description }}
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
      randomOutlet: function() {
        if (store.state.articles) {
          let random = Object.keys(store.state.articles)[Math.floor(Math.random() * Object.keys(store.state.articles).length)]
          console.log("random outlet", random)
          return temp
        } else {
          return "loading..."
        }
      },
      computedArticles: function(){
        console.log("in Home Banner computed:", store.state.articles)
        if (store.state.articles) {
          return store.state.articles
        } else {
          return "loading..."
        }
      }
    },
    methods: {
      // TODO
      goArticle() {
        this.$router.push({ path: `/article/${this.computedArticles.id-1}` }) 
      },
    },
  }
</script>

