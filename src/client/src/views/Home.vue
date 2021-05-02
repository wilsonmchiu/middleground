<template>
  <v-container>
    <HomeBanner :img_src="banner_img_src" :title="banner_title" :desc="banner_desc"/>
    <GalleryBox :title="aTitle" :imgLink="imgLink" > </GalleryBox>
  </v-container>
</template>

<script>
  import HomeBanner from '../components/HomeBanner'
  import GalleryBox from "../components/GalleryBox"

  export default {
    name: 'Home',

    data:() => ({
      banner_img_src: "https://i0.wp.com/johnnyalucard.com/wp-content/uploads/2020/04/shrek.jpg",
      banner_title: "Top story",
      banner_desc: "hahahah",
      aTitle: "ww",
      imgLink: "https://cdn.pixabay.com/photo/2020/07/12/07/47/bee-5396362_1280.jpg",
    }),

    components: {
      HomeBanner,
      GalleryBox,
    },
  }
</script>
