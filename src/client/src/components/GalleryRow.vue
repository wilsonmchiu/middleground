<!-- GalleryRow.vue -->
<template>
  <v-container>

    <h1 style=font-size:300%;font-family:Courier New>{{ header }}</h1>
  
     <v-carousel hide-delimiters height="300px"> 
        <template v-for="(item, index) in imgLinks"> 
          <v-carousel-item v-if="(index + 1) % columns === 1 || columns === 1" 
           :key="index"
          > 
            <v-row class="flex-nowrap" style="height:100%"> 
              <template v-for="(n,i) in columns"> 
                <template v-if="(+index + i) < imgLinks.length"> 
                  <v-col :key="i"> 

                    <gallery-box v-if="(+index + i) < imgLinks.length"
                    :title="titles[+index + i]" :imgLink="imgLinks[+index + i]" :url="urls[+index + i]">
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
    props: ["header", "imgLinks", "titles", "urls"],
    components: {
      'gallery-box': GalleryBox
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
    }
  };
</script>
