<style>
  .v-card__text, .v-card__title {
    word-break: normal; /* maybe !important  */
  }
</style>

<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm = "12" md="8" lg="8" style="padding-bottom: 200px">
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
          {{currentArticle.content}}<br/>
          <a :href=currentArticle.url>{{currentArticle.url}}</a><br/>
          <v-divider style="margin-top:10px"></v-divider>
          <br/>
          Please purchase the full news API or visit the link above to read the rest of the article!<br/>
          <br/>
          Here's a lorem ipsum to fill space that would be there normally: <br/>
          {{tempContent}}
        </v-card-text>
        <v-card-text>
          <h1 style="display:inline;padding-right:20px">Middle Ground </h1>
          <h3 style="display:inline;">{{comments.length}} comments</h3>
          <v-divider style="margin-top:10px"></v-divider>
        </v-card-text>
        <v-text-field
          prepend-icon="mdi-account"
          v-model="commentForm"
          :placeholder="commentForm"
          :counter="160"
          :maxlength=160
          label="Write Comment Here"
          @click="showCommentButtons = true"
          @keydown.enter="postComment(currentArticle.id); showCommentButtons = false"
        ></v-text-field>
        <v-btn
          v-show="showCommentButtons"
          text
          small
          color="blue darken-4"
          class="justify-start px-6 ml-4 mt-n6"
          :ripple="false"
          @click="postComment(currentArticle.id); showCommentButtons = false"
          >Post Comment
        </v-btn>
        <v-btn
          v-show="showCommentButtons"
          text
          small
          color="red darken-4"
          class="justify-start px-6 ml-4 mt-n6"
          :ripple="false"
          @click="showCommentButtons = false"
          >Cancel
        </v-btn>

        <div v-for="comment in comments" :key="comment.id">
          <comment @deleteComment="deleteComment" :id="comment.id" :author="comment.username" :date="comment.date" :content="comment.content" :replies="comment.replies"></comment>
        </div>
      </v-col>

      <v-col cols="12" sm= "12" md="4" lg="4">
        <h4 class="mb-3 mt-3">Related</h4>

        <div v-for="(card,index) in relatedCards" :key="index" class="mb-5">
          <v-skeleton-loader
            class="mx-auto"
            type="list-item-avatar-three-line"
            tile
            large
          >
            <v-card class="card" tile flat @click="goArticle(card.id)">
              <v-row no-gutters>
                <v-col class="mx-auto" cols="3" sm="3" md="5" lg="5">
                  <v-img
                    class="align-center"
                    :src="card.urlToImage"
                  >
                  </v-img>
                </v-col>
                <v-col class="ml-2" cols="6">
                  <div >
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
  import axios from 'axios';
  import Comment from "../components/Comment.vue"
  import {store} from "../store.js";
  
  export default {
    name: 'Article',
    components: {
      'comment': Comment
    },
    data() {
      return {
        isAuthenticated : this.$session.exists(),
        currentUser: this.$session.get('username'),
        commentForm: "",
        showCommentButtons: false,
        tempContent: "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, \n\nconsectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered \n\n\n\n the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical \n\nLatin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of \n\nclassical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.",
        currentArticleId: this.$route.params.id,
        currentArticleOutlet: this.$route.params.outlet,
        apiRoot: process.env.VUE_APP_API_ROOT,
        comments: [],
        avatar: "https://cdn2.iconfinder.com/data/icons/facebook-51/32/FACEBOOK_LINE-01-512.png"
      };
    },
    computed: {
      currentArticle: function(){
        if (store.state.articles && Object.keys(store.state.articles).length > 0) {
          return store.state.articles[this.currentArticleOutlet].find(article => article.id == this.currentArticleId);
        } else {
          return {id:"loading...", title:"loading...", author:"loading...", publishedAt:"loading...", urlToImage:"loading...", comments:"loading..."}
        }
      },
      relatedCards: function(){
        if (store.state.articles && Object.keys(store.state.articles).length > 0) {
          let outlet = store.state.articles[this.currentArticleOutlet].filter((item)=> item.id!=this.currentArticleId)
          return outlet.slice(0,10)
        } else {
          return [{id:"loading...", title:"loading...", author:"loading...", publishedAt:"loading...", urlToImage:"loading..."}]
        }
      },
    },
    created(){
      this.getComments();
    },
    methods: {
      deleteComment(id) {
        this.comments = this.comments.filter(item => item.id != id);
      },
      getComments() {
        const path = `${this.apiRoot}/comments/get`;
        axios
          .get(path, {
            params: {
              articleID: this.currentArticleId,
            }
          })
          .then((response) => {
            console.log('Getting comments: ', response.data.comments)
            this.comments = response.data.comments;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      postComment(uniqueArticleId) {
        const path = `${this.apiRoot}/comments/post`;
        const payload = {
          username: this.currentUser,
          articleID: uniqueArticleId,
          userComment: this.commentForm,
        };
        console.log(payload);
        if (this.isAuthenticated === false) {
          this.$router.push("/login");
        }
        else if (this.commentForm != "") {
          axios
          .post(path, payload)
          .then((response) => {
            this.comments.push(response.data.newComment);
          })
          .catch((error) => {
            console.log(error);
          });
        }
        this.commentForm = "";
      },
      goArticle(articleID) {
        this.$router.push({ path: `/${this.currentArticleOutlet}/${articleID}` }) 
        window.scrollTo(0,0);
      },
    },
  };
</script>