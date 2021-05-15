<style>
  .v-card__text, .v-card__title {
    word-break: normal; /* maybe !important  */
  }
</style>

<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm = "12" md="8" lg="8">
        <v-card-text>
          <h1>{{currentArticle.title}}</h1>
          <br>
          <v-list-item-subtitle>By {{currentArticle.author}}</v-list-item-subtitle>      
          <v-list-item-subtitle>{{currentArticle.publishedAt}}</v-list-item-subtitle>
        </v-card-text>
        <v-img 
          :aspect-ratio="2/1"
          :src="currentArticle.urlToImage">
        </v-img>
        <v-card-text>
          {{tempContent}}
        </v-card-text>
        <v-card-text>
          <h1>Middle Ground </h1>
          <subtitle-1>{{comments.length}} comments</subtitle-1>
        </v-card-text>
        <v-text-field
          :counter="160"
          label="Write Comment Here"
        ></v-text-field>

        <v-row class="justify-space-between">
          <v-col >
            <div v-for="comment in comments" :key="comment">
              <comment :author="comment.author" :contents="comment.contents" :avatar="comment.avatar"></comment>
            </div>
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="12" sm= "12" md="4" lg="4">
        <hr class="grey--text" />
        <h4 class="mb-3 mt-3">What People Think</h4>
        <v-img 
          :aspect-ratio="5/1"
          src="https://canvasjs.com/wp-content/uploads/images/gallery/javascript-charts/overview/javascript-charts-graphs-index-data-label.png"></v-img>
        <h4 class="mb-3 mt-3">Related</h4>

        <div v-for="(card,index) in relatedCards" :key="index" class="mb-5">
          <v-skeleton-loader
            class="mx-auto"
            type="list-item-avatar-three-line"
            tile
            large
          >
            <v-card class="card" tile flat>
              <v-row no-gutters>
                <v-col class="mx-auto" cols="3" sm="3" md="5" lg="5">
                  <v-img
                    class="align-center"
                    :src="card.urlToImage"
                  >
                  </v-img>
                </v-col>
                 <v-col>
                  <div class="ml-2">
                    <v-card-title
                      class="pl-2 pt-0 subtitle-1 font-weight-bold"
                      style="line-height: 1"
                    >
                      {{card.title}}
                    </v-card-title>

                    <v-card-subtitle
                      class="pl-2 pt-2 pb-0"
                      style="line-height: 1"
                    >
                      {{card.author}}<br />
                      {{card.publishedAt}}
                    </v-card-subtitle>
                  </div>
                </v-col> 
              </v-row>
            </v-card>
          </v-skeleton-loader>
        </div> 
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  // import axios from 'axios';
  import Comment from "../components/Comment.vue"
  import {store} from "../store.js";


  export default {
    name: 'Article',
    components: {
      'comment': Comment
    },
    data() {
      return {
        comments: [],
        tempContent: "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, \n\nconsectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered \n\n\n\n the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical \n\nLatin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of \n\nclassical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.",
         currentArticleId: this.$route.params.id,
         currentArticleOutlet: this.$route.params.outlet,
      }
    },
    created(){
        this.comments = [
          {
          "author": "Adam Smith",
          "contents": "It is not from the benevolence of the butcher, the brewer, or the baker that we expect our dinner, but from their regard to their own interest. All money is a matter of belief",
          "avatar": "https://i.cbc.ca/1.5303387.1583953990!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_780/adam-smith-the-muir-portrait-circa-1800.jpg"
          },
          {
          "author": "George Washington",
          "contents": "It is better to offer no excuse than a bad one. It is better to be alone than in bad company. If freedom of speech is taken away, then dumb and silent we may be led, like sheep to the slaughter.",
          "avatar": "https://www.history.com/.image/ar_16:9%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_faces:center%2Cq_auto:good%2Cw_620/MTcwNDY1NDEzNzMyNDQzOTMy/wshington_timeline.jpg"
          }
        ]
      },
    computed: {
      currentArticle: function(){
        if (store.state.articles && Object.keys(store.state.articles).length > 0) {
          return store.state.articles[this.currentArticleOutlet][this.currentArticleId]
        } else {
          return {title:"loading...", author:"loading...", publishedAt:"loading...", urlToImage:"loading..."}
        }
      },
      relatedCards: function(){
        if (store.state.articles && Object.keys(store.state.articles).length > 0) {
          let outlet = store.state.articles[this.currentArticleOutlet].filter((_, index)=> index!=this.currentArticleId)
          return outlet.slice(0,10)
        } else {
          return [{title:"loading...", author:"loading...", publishedAt:"loading...", urlToImage:"loading..."}]
        }
      },
    },
  }
</script>