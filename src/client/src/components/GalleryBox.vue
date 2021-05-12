<template>
  <v-container class="pa-0">
  <v-hover v-slot:default="{ hover }">
    <v-sheet
      class="mx-auto"
      height="100%"
      @click="goArticle"
      :elevation="hover ? 24 : 0"
    >
      <v-img
        :src="urlToImage"
        :aspect-ratio="6/5"
      >
      </v-img>
    </v-sheet>
    
  </v-hover>
  <h6 style=color:black;font-size:100%;font-family:Courier>{{title}}</h6>
  </v-container>
</template>

<script>
export default {
  props: ["title", "urlToImage", "id", "outlet"],
  methods: {
    goArticle() {
      // this.$router.push("/article/" + (this.id-1))
      this.$router.push({ path: `/${this.outlet}/${this.id}` }) 
    },
  },
};
</script>

