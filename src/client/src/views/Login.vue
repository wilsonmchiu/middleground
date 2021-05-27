<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 80%;
}
.login-background{
  background: linear-gradient(to right, rgba(0,0,255,.2) 0%, rgba(0,0,255,.2) 40%, rgba(255,0,0,.2) 60%, rgba(255,0,0,.2) 100%);
}
</style>

<template>
  <v-container fluid class="fill-height login-background">
    <v-row>
      <v-col cols="12" xs="12" sm="6" md="4" lg="3" class="ma-auto">
        <img :src="logo" class="center">
        <v-card class="pa-1" style="background-color:black">
          <v-card class="px-6 pt-10 pb-16">
            <h3 class="text-center mb-4">Log In</h3>
            <alert v-if="showError" :msg="alertMessage"> </alert>
            <v-text-field solo dense v-model="username" label="Enter Username" required> </v-text-field>
            <v-text-field solo dense v-model="password" label="Password" type="password" required></v-text-field>
            <v-btn tile block color="rgba(0, 0, 0, 0.67)" class="mt-6 mr-4 white--text" @click="onSubmit"> Login </v-btn>
          </v-card>
        </v-card>
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
      apiRoot: process.env.VUE_APP_API_ROOT,
      token: "",
      logo: require('../assets/static/logo.png')
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
};
</script>