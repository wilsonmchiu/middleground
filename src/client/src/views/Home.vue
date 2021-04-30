<template>
  <v-container>
    <HomeBanner :img_src="banner_img_src" :title="banner_title" :desc="banner_desc"/>
  </v-container>
</template>

<script>
  import HomeBanner from '../components/HomeBanner'

  export default {
    name: 'Home',

    data:() => ({
      banner_img_src: "https://i0.wp.com/johnnyalucard.com/wp-content/uploads/2020/04/shrek.jpg",
      banner_title: "Top story",
      banner_desc: "hahahah"
    }),

    components: {
      HomeBanner,
    },
  }
</script>
