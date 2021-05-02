<!-- GalleryRow.vue -->
<template>
  <v-container>
  
     <v-carousel hide-delimiters> 
        <template v-for="(item, index) in imgLinks"> 
          <v-carousel-item v-if="(index + 1) % columns === 1 || columns === 1" 
           :key="index"
          > 
            <v-row class="flex-nowrap" style="height:100%"> 
              <template v-for="(n,i) in columns"> 
                <template v-if="(+index + i) < imgLinks.length"> 
                  <v-col :key="i"> 

                    <gallery-box v-if="(+index + i) < imgLinks.length"
                    :title="titles[i]" :imgLink="imgLinks[+index + i]">
                      <v-row class="fill-height"
                       align="center"
                       justify="center"
                      >
                        <div class="display-3">{{+index + i + 1}}</div>
                      </v-row>
                    </gallery-box>
                    
                  </v-col> 
                </template> 
              </template> 
            </v-row> 
          </v-carousel-item> 
        </template> 
      </v-carousel>  
  </v-container>
</template>

<script>
  import GalleryBox from "./GalleryBox.vue"

  export default {
    components: {
      'gallery-box': GalleryBox
    },
    data(){
    return {
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
      ],
      titles: [
          'First',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
          'First',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
        ],
    }
  },
  computed: {
    columns() {
      if (this.$vuetify.breakpoint.xl) {
        return 4;
      }

      if (this.$vuetify.breakpoint.lg) {
        return 3;
      }

      if (this.$vuetify.breakpoint.md) {
        return 2;
      }

      return 1;
    }
  },
  };
</script>
