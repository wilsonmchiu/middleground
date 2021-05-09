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
import store from "./store.js"

export default {
  name: 'App',
  data() {
    return {
      isAuthenticated : this.$session.exists(),
      username: this.$session.get('username'),
      logo: require('./assets/static/logo.png'),
      numbers: store.state.numbers.join()
    };
  },
  components: {
    navBar: NavBar,
  },
  created(){
   console.log("app created");
   console.log("state: ", store.state.numbers);
  }
};
</script>
