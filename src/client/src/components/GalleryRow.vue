<!-- GalleryRow.vue -->
<template>
      <v-container height="100%" class="px-0">
       <h1 class="text-capitalize" style=font-size:200%;font-family:palatino linotype>{{ headerFinal }}</h1>
      <v-carousel  hide-delimiters height="auto" width="auto"> 
        <template v-for="(item, index) in articles"> 
          <v-carousel-item v-if="(index + 1) % columns === 1 || columns === 1" 
                           :key="index"
          > 
            <v-row class="flex-nowrap" style="height:100%"> 
              <template v-for="(n,i) in columns"> 
                <template v-if="(+index + i) < articles.length"> 
                  <v-col :key="i"> 
                    <gallery-box v-if="(+index + i) < articles.length"
                    :title="articles[+index + i].title" :urlToImage="articles[+index + i].urlToImage" :url="articles[+index + i].url"
                    :outlet="header" :articleID="articles[+index + i].id"  :description="articles[+index+i].description">
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

    data() {
    return {
      headerFinal: this.formatHeader(this.header),
    };
  },
    components: {
      'gallery-box': GalleryBox
    },
    methods:{
      refreshOnResize(){
        this.$(window).resize(function(){
          this.$forceUpdate();
        });
      },
      formatHeader(header){
        header = header.replace(/-/g, ' ');
        header.toUpperCase()
        return header      
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

      },
    },
  };
</script>
