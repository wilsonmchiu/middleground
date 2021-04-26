<template>
  <GalleryBox :title="aTitle" :imgLink="imgLink" > </GalleryBox>
</template>

<script>
  import GalleryBox from "../components/GalleryBox"

  export default {
    name: 'Home',

    components: {
      GalleryBox,
    },

    data() {
      return {
        aTitle: "ww",
        imgLink: "https://cdn.pixabay.com/photo/2020/07/12/07/47/bee-5396362_1280.jpg",
      };
    },
  }
</script>
