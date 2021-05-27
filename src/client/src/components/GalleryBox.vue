<template>
  <v-container class="pa-0">
  <v-hover v-slot:default="{ hover }">
    <a>
      <v-sheet
        class="rounded-xl"
        max-width="900px"
        @click="goArticle"
        :elevation="hover ? 24 : 0"
      >
        <v-img
        class="rounded-xl"
          :src="urlToImage"
          :aspect-ratio="6/5"
          max-height="400px"
          gradient="to bottom, rgba(255, 255, 255, 0.10), rgba(0, 0, 0, 0.90)"
        >
          <h6 class="pr-4" style="color:white;font-size:100%;position:absolute;
          bottom:8px;left:16px;">{{title}}</h6>
        </v-img>

      </v-sheet>
    </a>
  </v-hover>
  </v-container>
</template>

<script>
export default {
  props: ["title", "urlToImage", "outlet", "articleID"],
  methods: {
    goArticle() {
      this.$router.push({ path: `/${this.outlet}/${this.articleID}` }) 
      window.scrollTo(0,0);
    },
  },
};
</script>

