<template>
  <v-container>
    <v-card-text>
      <h1>Login</h1>
    </v-card-text>
    <alert v-if="showError" :msg="alertMessage"> </alert>
    <v-text-field v-model="username" label="username" required> </v-text-field>
    <v-text-field v-model="password" label="password" type="password" required></v-text-field>

    <v-btn color="success" class="mr-4" @click="onSubmit"> Login </v-btn>
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
      console.log(payload);
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
          console.log(error);
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