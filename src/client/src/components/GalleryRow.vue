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
                    <v-sheet v-if="(+index + i) < imgLinks.length" 
                     :color="imgLinks[+index + i]" height="100%"
                    >
                    <gallery-box v-if="(+index + i) < imgLinks.length"
                    :title="titles[i]" :imgLink="imgLinks[+index + i]">
                      <v-row class="fill-height"
                       align="center"
                       justify="center"
                      >
                        <div class="display-3">{{+index + i + 1}}</div>
                      </v-row>
                    </gallery-box>
                    </v-sheet>
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
  

  export default {
    data(){
    return {
      imgLinks: [
        'https://picsum.photos/id/11/500/300',
        'https://picsum.photos/id/12/500/300',
        'https://picsum.photos/id/13/500/300',
        'https://picsum.photos/id/14/500/300',
        'https://picsum.photos/id/15/500/300',
      ],
      titles: [
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
