<template>
  <v-hover v-slot:default="{ hover }">
    <v-card
      class="mx-auto"
      max-width="300"
      @click="onClick"
      :elevation="hover ? 24 : 0"
    >
      <v-img
        class="white--text align-end"
        height="400px"
        :src="imgLink"
      >
        <v-card-title>{{ title }}</v-card-title>
      </v-img>

    </v-card>
  </v-hover>
</template>

<script>
export default {
  props: ["title", "imgLink"],

  methods: {
    onClick() {
      this.$router.push("/")
    },
  },
};
</script>