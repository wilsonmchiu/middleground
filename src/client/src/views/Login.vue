<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 80%;
}
.login-background{
  background: linear-gradient(to right, rgba(0,0,255,.2) 0%, rgba(0,0,255,.2) 40%, rgba(255,0,0,.2) 60%, rgba(255,0,0,.2) 100%);
}
.guest {
  position: absolute; 
  bottom:0; 
  right:0;
  padding-right: 40px;
  padding-bottom: 40px;
  text-decoration-line: underline;
  font-family: Poppins;
}
a {
  text-decoration-line: underline;
  font-family: Poppins;
}
</style>

<template>
  <v-container fluid class="fill-height login-background">
    <v-row>
      <v-col cols="12" xs="12" sm="6" md="4" lg="3" class="ma-auto">
        <img :src="croppedLogo" class="center">
        <v-card class="pa-1" style="background-color:black">
          <v-card class="px-6 pt-10 pb-16">
            <h3 class="text-center mb-4">Log In</h3>
            <alert v-if="showError" :msg="alertMessage"> </alert>
            <alert v-if="comingSoonAlert" msg="Social media buttons coming soon"> </alert>
            <v-text-field solo dense v-model="username" label="Enter Username" required> </v-text-field>
            <v-text-field solo dense v-model="password" label="Password" type="password" required></v-text-field>
            <v-btn tile block color="rgba(0, 0, 0, 0.67)" class="mt-6 mr-4 white--text" @click="onSubmit"> Login </v-btn>
            <v-img :src="login_google_FB_button" class="mt-6" style="width:100%" @click="comingSoonAlert=true; showError=false"></v-img>
            <v-row justify="center" class="mt-4"><a href="/register" style="color:black">Need to Register?</a></v-row>
          </v-card>
        </v-card>
        <a href="/" class="guest" style="color:black">continue as guest</a>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
//import Vue from 'vue';
import axios from "axios";
import Alert from "../components/Alert.vue";
import {store} from "../store.js";

export default {
  components: {
    alert: Alert,
  },
  data() {
    return {
      username: "",
      password: "",
      response: "",
      alertMessage: "",
      showError: false,
      comingSoonAlert: false,
      apiRoot: process.env.VUE_APP_API_ROOT,
      token: "",
      login_google_FB_button: require('../assets/login_google_FB_button.png'),
      croppedLogo: require('../assets/static/croppedLogo.png')
    };
  },
  methods: {
    initForm() {
      this.username = "";
      this.password = "";
    },
    validate() {
      if (this.username === "" || this.password === "") {
        this.showError = true;
        this.alertMessage = "Please enter username and/or password";
        return false;
      }
      return true;
    },
    async login(payload) {
      axios
        .post(`${this.apiRoot}/auth/login`, payload)
        .then((response) => {
          if (response.data["auth"] === "success") {
            this.$session.start();
            this.$session.set("jwt", response.data["token"]);
            this.$session.set("username", this.username);
            this.$emit('justLoggedIn', true);
            this.$router.push("/");
            store.login(this.username);
          } 
        })
        .catch((error) => {
          this.alertMessage = error.response.data["msg"];
          this.showError = true;
        });
    },
    onSubmit(evt) {
      this.comingSoonAlert=false;
      evt.preventDefault();
      const payload = {
        username: this.username,
        password: this.password,
      };
      if(this.validate())
        this.login(payload);
      else
        this.initForm();
    },
  },
  created(){
    //reroute if user is already logged in
    if(this.$session.exists()){
      this.$router.push("/");
    }
  }
};
</script>