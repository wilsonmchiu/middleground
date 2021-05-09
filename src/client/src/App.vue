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
import { store }from "./store.js"

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
      axios
        .get(`http://${this.apiRoot}/news`)
        .then((response) => {
          console.log(response);
          store.setArticles(response.data.articles)
          this.articlesRetrieved = true
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
   console.log("app created");
   await this.getArticles();
   console.log("article: ", store.state.articles);
  }
};
</script>

