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
export default {
  name: 'App',
  data() {
    return {
      isAuthenticated : this.$session.exists(),
      username: this.$session.get('username'),
      logo: require('./assets/static/logo.png')
    };
  },
  components: {
    navBar: NavBar,
  }
};
</script>
