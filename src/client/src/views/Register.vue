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
.link {
  position: absolute; 
  bottom:0; 
  right:0;
  padding-right: 30px;
  padding-bottom: 40px;
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
            <form action = "/user/checkout" method="POST"></form>
            <h3 class="text-center mb-4">Register</h3>
            <alert v-if="showError" :msg="alertMessage"> </alert>
            <alert v-if="comingSoonAlert" msg="Social media buttons coming soon"> </alert>
            <v-text-field solo dense v-model="username" label="Enter Username" required> </v-text-field>
            <v-text-field solo dense v-model="password" label="Password" type="password" required></v-text-field>
            <v-btn tile block color="rgba(0, 0, 0, 0.67)" class="mt-6 mr-4 white--text" @click="onSubmit"> Register </v-btn>
            <v-img :src="google_button" class="mt-2" @click="comingSoonAlert=true; showError=false"></v-img>
            <v-img :src="facebook_button" class="mt-2" @click="comingSoonAlert=true; showError=false"></v-img>
            <a href="/login" class="link" style="color:black">Already Registered?</a>
          </v-card>
        </v-card>
        <a href="/" class="guest" style="color:black">continue as guest</a>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import Alert from "../components/Alert.vue";


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "XCSRF-TOKEN";

export default {
  components: {
    "alert": Alert,
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
      logo: require('../assets/static/logo.png'),
      google_button: require('../assets/google_button.png'),
      facebook_button: require('../assets/facebook_button.png'),
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
        this.initForm();
      }
    },
    onSubmit(evt) {
      this.comingSoonAlert=false;
      evt.preventDefault();
      const path = `${this.apiRoot}/auth/register`;
      const payload = {
        username: this.username,
        password: this.password,
      };
      this.validate();
      axios
        .post(path, payload)
        .then((response) => {
          if (response.data["insert_status"] === "success") {
            this.$router.push("/login");
          } 
        })
        .catch((error) => {
          this.alertMessage = error.response.data["msg"];
          this.showError = true;
          this.initForm();
        });
      this.initForm();
    },
  },
};
</script>