<template>
  <v-hover v-slot:default="{ hover }">
    <v-sheet
      class="mx-auto"
      @click="goArticle"
      :elevation="hover ? 24 : 0"
    >
      <v-img
        class="white--text align-end"
        :src="imgLink"
        gradient="to bottom, rgba(255,255,255,0) 60%, rgba(0,0,0,1)"
      >
        <v-card-title>{{ title }}</v-card-title>
      </v-img>

    </v-sheet>
  </v-hover>
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