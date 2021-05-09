<template>
  <v-container>
  <home-banner :img_src="banner_img_src" :title="banner_title" :desc="banner_desc"/>
   <gallery-row :header="header" :articles="articles"></gallery-row>
   <gallery-row :header="header2" :articles="articles"></gallery-row>

  </v-container>
</template>

<script>
import GalleryRow from '../components/GalleryRow';
import HomeBanner from '../components/HomeBanner'


  export default {
    name: 'Home',

    data:() => ({
      /*Banner Fields*/
      banner_img_src: "https://i0.wp.com/johnnyalucard.com/wp-content/uploads/2020/04/shrek.jpg",
      banner_title: "Top story",
      banner_desc: "hahahah",

      /*Gallery Row Fields Start*/
      header: "Header 1",
      header2: "Header 2",
      articles: [
          //#TODO to be loaded from the database
          {imgLink:'https://picsum.photos/id/11/500/300', title: "Title 1", url: "register/" },
          {imgLink:'https://picsum.photos/id/12/500/300', title: "Title 2", url: "#" },
          {imgLink:'https://picsum.photos/id/13/500/300', title: "Title 3", url: "#" },
          {imgLink:'https://picsum.photos/id/14/500/300', title: "Title 4", url: "#" },
          {imgLink:'https://picsum.photos/id/15/500/300', title: "Title 5", url: "#" },
          {imgLink:'https://picsum.photos/id/16/500/300', title: "Title 6", url: "#" },
          {imgLink:'https://picsum.photos/id/17/500/300', title: "Title 7", url: "#" },
          {imgLink:'https://picsum.photos/id/18/500/300', title: "Title 8", url: "#" },
          {imgLink:'https://picsum.photos/id/19/500/300', title: "Title 9", url: "#" },
          {imgLink:'https://picsum.photos/id/20/500/300', title: "Title 10", url: "#" },
          {imgLink:'https://picsum.photos/id/21/500/300', title: "Title 11", url: "#" },
          {imgLink:'https://picsum.photos/id/22/500/300', title: "Title 12", url: "#" },
        ],
    }),

    components: {
      'gallery-row': GalleryRow,
      'home-banner':HomeBanner,
    },
    methods: {
      getLists(){
        /*
        This function will make an axios 
        call to server for list of "article"\

        this.articles = axios... .

        to be called in beforeMount
        */
      }
    },
    beforeMount(){
      /*#TODO 
        1) Load lists into data "articles" field
      */ 
    },
  }
</script>
