<!-- GalleryRow.vue -->
<template>
      <v-container>
       <h1 style=font-size:200%;font-family:Courier New>{{ header }}</h1>
      <v-carousel hide-delimiters height="auto" width="auto"> 
        <template v-for="(item, index) in titles"> 
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
    props: ["header", "articles"],
    components: {
      'gallery-box': GalleryBox
    },
    data() {
      return {
        imgLinks: [],
        titles: [],
        urls: [],
      }
    },
    methods:{
      refreshOnResize(){
        this.$(window).resize(function(){
          this.$forceUpdate();
        });
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
     mounted(){
      for( const article of this.articles){
        this.imgLinks.push(article["imgLink"])
        this.titles.push(article["title"])
        this.urls.push(article["url"])
      }
    
    }
  };
</script>
