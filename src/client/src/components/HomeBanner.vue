<template>
  <v-container>
    <a>
      <v-row class="banner-container" 
      @click="goArticle">
        <v-col lg="8" md="8" sm="8" class="pa-0">
          <v-parallax
          :src="article.urlToImage"
          height=500
          >
          </v-parallax>
        </v-col>
        <v-col lg="4" md="4" sm="4">
            <h1 class="banner-text">
               {{ article.title }}
            </h1>
            <br/>
            <p class="banner-text">
               {{ article.description }}
            </p>
        </v-col>
      </v-row>
    </a>
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
  export default {
    name: 'HomeBanner',
    props: ['article', 'path'],
    methods: {
      goArticle() {
          this.$router.push({ path: this.path }) 
      },
    },
  }
</script>

