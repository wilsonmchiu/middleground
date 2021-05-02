<template>
  <v-container>
  <!---<GalleryBox :title="aTitle" :imgLink="imgLink" > </GalleryBox>-->
  <gallery-row :header="header" :imgLinks="imgLinks" :titles="titles" :urls="urls"></gallery-row>
  <gallery-row :header="header2" :imgLinks="imgLinks2" :titles="titles2" :urls="urls2"></gallery-row>
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
        header: "Featured",
        imgLinks: [
          'https://picsum.photos/id/11/500/300',
          'https://picsum.photos/id/12/500/300',
          'https://picsum.photos/id/13/500/300',
          'https://picsum.photos/id/14/500/300',
          'https://picsum.photos/id/15/500/300',
          'https://picsum.photos/id/16/500/300',
          'https://picsum.photos/id/17/500/300',
          'https://picsum.photos/id/18/500/300',
          'https://picsum.photos/id/19/500/300',
          'https://picsum.photos/id/20/500/300',
          'https://picsum.photos/id/21/500/300',
          'https://picsum.photos/id/22/500/300',
        ],
        titles: [
          'Title 1',
          'Title 2',
          'Title 3',
          'Title 4',
          'Title 5',
          'Title 6',
          'Title 7',
          'Title 8',
          'Title 9',
          'Title 10',
          'Title 11',
          'Title 12',
        ],
        urls: [
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
        ],
        header2: "Hot",
        imgLinks2: [
          'https://picsum.photos/id/23/500/300',
          'https://picsum.photos/id/24/500/300',
          'https://picsum.photos/id/25/500/300',
          'https://picsum.photos/id/26/500/300',
          'https://picsum.photos/id/27/500/300',
          'https://picsum.photos/id/28/500/300',
          'https://picsum.photos/id/29/500/300',
          'https://picsum.photos/id/30/500/300',
          'https://picsum.photos/id/31/500/300',
          'https://picsum.photos/id/32/500/300',
          'https://picsum.photos/id/33/500/300',
          'https://picsum.photos/id/34/500/300',
        ],
        titles2: [
          'Title 1',
          'Title 2',
          'Title 3',
          'Title 4',
          'Title 5',
          'Title 6',
          'Title 7',
          'Title 8',
          'Title 9',
          'Title 10',
          'Title 11',
          'Title 12',
        ],
        urls2: [
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
          '#',
        ],
      };
    },
  }
</script>
