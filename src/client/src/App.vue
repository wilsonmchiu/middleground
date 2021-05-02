<template>
  <v-app>

    <v-app-bar color="primary" app dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>
      <v-spacer></v-spacer>
      <v-btn @click="logout">
        <span v-if="isAuthenticated" class="mr-2">{{ username }}</span>
        <span v-else class="mr-2">Login</span>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isAuthenticated : this.$session.exists(),
      username: this.$session.get('username')
    };
  },
  methods:{
    logout(){
      if(this.isAuthenticated){
        this.$session.destroy();
        this.isAuthenticated = false;
      } else {
        this.$router.push(`/login`);
      }
    },
    goToLogin(){
    }
  },
};
</script>
