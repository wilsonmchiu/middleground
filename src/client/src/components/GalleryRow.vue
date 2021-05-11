<!-- GalleryRow.vue -->
<template>
      <v-container class="px-0">
       <h1 style=font-size:200%;font-family:Courier New>{{ header }}</h1>
      <v-carousel hide-delimiters height="auto" width="auto"> 
        <template v-for="(item, index) in computedArticles"> 
          <v-carousel-item v-if="(index + 1) % columns === 1 || columns === 1" 
                           :key="index"
          > 
            <v-row class="flex-nowrap" style="height:100%"> 
              <template v-for="(n,i) in columns"> 
                <template v-if="(+index + i) < computedArticles.length"> 
                  <v-col :key="i" class="pr-0"> 
                    <gallery-box v-if="(+index + i) < computedArticles.length"
                    :title="computedArticles[+index + i].title" :urlToImage="computedArticles[+index + i].urlToImage" :url="computedArticles[+index + i].url"
                    :id="computedArticles[+index + i].id">
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
  import {store} from "../store.js";

  export default {
    props: ["header"],
    components: {
      'gallery-box': GalleryBox
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
      },
      computedArticles: function(){
        console.log("in Gallery Row computed:", store.state.articles)
        if (store.state.articles && store.state.articles.length>0)
          return store.state.articles
        return "loading..."
      }
    },
  };
</script>
