<template>
  <v-app-bar color="white" app dark>

    <div @click="base" class="d-flex align-center">
      <a>
        <v-img class="shrink mr-2" contain :src="logo" 
        transition="scale-transition" width="200"/>
      </a>
    </div>

    <v-spacer></v-spacer>

    <v-menu offset-y v-if="isAuthenticated">
      <template v-slot:activator="{ on, attrs }">
        <v-btn v-if="isAuthenticated" class="mr-2 pl-6 pr-6"
        color="black" v-bind="attrs" v-on="on" text>
          <v-icon class="mr-2">mdi-account</v-icon>
          <h2 class="text-capitalize">{{ username }}</h2>
        </v-btn>
      </template>
      <v-list>
        <v-list-item-group >
          <v-list-item>
            <v-icon class="mr-2" small>mdi-pencil</v-icon>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-icon class="mr-2" small>mdi-lock</v-icon>
            <v-list-item-title>Privacy</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-icon class="mr-2" small>mdi-bookmark</v-icon>
            <v-list-item-title>Bookmarked</v-list-item-title>
          </v-list-item>
          <v-list-item @click="logout">
            <v-icon class="mr-2" small>mdi-power</v-icon>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-menu>

    <v-btn @click="register" v-if="!isAuthenticated" class="mr-2">
      <span>Register</span>
    </v-btn>
    <v-btn @click="login" v-if="!isAuthenticated" class="mr-2">
      <span>Login</span>
    </v-btn>

  </v-app-bar>
</template>

<script>
import {store} from "../store.js";
export default {

  data() {
    return {
      logo: require('../assets/static/logo.png')
    };
  },
  computed:{
      isAuthenticated : function(){ 
        if(!store.state.isAuthenticated && this.$session.exists())
          store.login(this.$session.get('username'))
       return store.state.isAuthenticated
      },
      username: function(){
        
        return store.state.username
      },
  },
  methods:{
    base() {
      this.$router.push("/")
    },
    home() {
      this.$router.push("/home")
    },
    register() {
      this.$router.push("/register")
    },
    login(){
      this.$router.push(`/login`);
    },
    logout(){
      this.$session.destroy();
      store.logout()
    }
  }
};
</script>