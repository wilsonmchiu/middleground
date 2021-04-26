<template>
  <v-container>
    <v-row
      justify="space-around"
    >
      <gallerybox v-for="(title, imgLink)"></gallerybox>
    </v-row>
  </v-container>
</template>

<script>
  import GalleryBox from "./GalleryBox"

  export default {
    props: {
      boxes: Array,
    }

    components: {
      galleryBox: GalleryBox,
    }
  };
</script>