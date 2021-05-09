<template>
  <v-app>

    <navBar></navBar>
    <v-main>
      <router-view/>
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
      apiRoot: process.env.VUE_APP_API_ROOT,
      articlesRetrieved: false
    };
  },
  methods: {
    
    async getArticles() {
      await axios
        .get(`http://${this.apiRoot}/news`)
        .then((response) => {
          console.log("in App methods", response);
          console.log("in App methods", response.data.articles)
          console.log("in App methods", response.data.articles[0])
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

