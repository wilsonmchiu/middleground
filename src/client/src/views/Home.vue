<template>
  <v-container>
  <!---<GalleryBox :title="aTitle" :imgLink="imgLink" > </GalleryBox>-->
  <gallery-row></gallery-row>
  </v-container>
</template>

<script>
  //import GalleryBox from "../components/GalleryBox"
import GalleryRow from '../components/GalleryRow.vue';


  export default {
    name: 'Home',

    components: {
      'gallery-row': GalleryRow
    },

    data() {
      return {
        items: [
          {title: "ww",},
          {imgLink: "https://cdn.pixabay.com/photo/2020/07/12/07/47/bee-5396362_1280.jpg"}
        ],
        aTitle: "Title",
        imgLink: "https://cdn.pixabay.com/photo/2020/07/12/07/47/bee-5396362_1280.jpg",
      };
    },
  }
</script>
