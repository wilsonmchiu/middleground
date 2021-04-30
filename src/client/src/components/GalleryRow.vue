<!-- GalleryRow.vue -->
<template>
  <v-container>
  
    <v-carousel hide-delimiters :height="500">
    <v-row no-gutters class="fill-height">
      <v-container>
      <gallery-box :title="title" :imgLink="imgLink" > </gallery-box>
      <v-spacer></v-spacer>
      <gallery-box :title="title" :imgLink="imgLink" > </gallery-box>
      <v-spacer></v-spacer>
      <gallery-box :title="title" :imgLink="imgLink" > </gallery-box>
      <v-spacer></v-spacer>
      <gallery-box :title="title" :imgLink="imgLink" > </gallery-box>
      <v-spacer></v-spacer>
      <gallery-box :title="title" :imgLink="imgLink" > </gallery-box>
      </v-container>
    </v-row>
    </v-carousel>
  </v-container>
</template>

<script>
  import GalleryBox from "./GalleryBox"

  export default {
    data() {
      return {
        title: "hi",
        imgLink: "https://cdn.pixabay.com/photo/2020/07/12/07/47/bee-5396362_1280.jpg"
      }
    },
    props: {
     
    },
    components: {
      'gallery-box': GalleryBox,
    }
  };
</script>