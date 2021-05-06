<template>
  <v-container>
  <v-hover v-slot:default="{ hover }">
    <v-sheet
      class="mx-auto"
      height="100%"
      @click="goArticle"
      :elevation="hover ? 24 : 0"
    >
      <v-img
        :src="imgLink"
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
  props: ["title", "imgLink", "url"],
  methods: {
    goArticle() {
      this.$router.push(this.url)
    },
  },
};
</script>

