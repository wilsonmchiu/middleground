<template>
  <v-app>

    <navBar v-if="!['login', 'register'].includes($route.name)"></navBar>
    <v-main>
      <router-view :key="$route.fullPath"></router-view>
    </v-main>
  </v-app>
</template>

<script>
import NavBar from "./components/NavBar"
import axios from "axios";
import {store} from "./store.js"

export default {
  name: 'App',
  data() {
    return {
      isAuthenticated : this.$session.exists(),
      username: this.$session.get('username'),
      logo: require('./assets/static/logo.png'),
      apiRoot: process.env.VUE_APP_API_ROOT
    };
  },
  methods: {
    
    async getArticles() {
      Date.prototype.today = function () { 
          return this.getFullYear() + "-" + (((this.getMonth()+1) < 10)?"0":"") + (this.getMonth()+1) + "-" + ((this.getDate() < 10)?"0":"") + this.getDate();
      },
      Date.prototype.oneMonthBefore = function () { 
          return this.getFullYear() + "-" + (((this.getMonth()+1) < 10)?"0":"") + (this.getMonth()+1) + "-" + ((this.getDate() < 10)?"0":"") + this.getDate();
      }
      let newDate = new Date();
      await axios
        .get(`${this.apiRoot}/news`, {
          params: {
            partition_by: 'source', 
            limit_articles: 200, 
            publishedAt: [newDate.oneMonthBefore(), newDate.today()]
          }
        })
        .then((response) => {
          console.log("in App methods", response.data.articles)
          store.setArticles(response.data.articles)
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  components: {
    navBar: NavBar,
  },
  
  async created(){
   await this.getArticles();
   console.log("app created: ", store.state.articles);
  }
};
</script>

