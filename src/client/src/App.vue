<template>
  <v-app>

    <v-app-bar color="white" app dark>

      <div class="d-flex align-center">
        <v-img class="shrink mr-2" contain :src="logo" 
        transition="scale-transition" width="200"/>
      </div>
      <v-btn @click="home" class="ml-4" color="black" text>
        <h2 class="text-capitalize">Home</h2>
      </v-btn>
      <v-btn color="black" text>
        <h2 class="text-capitalize">About</h2>
      </v-btn>

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
          <v-list-item-group v-model="model">
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
          </v-list-item-group>
        </v-list>
      </v-menu>

      
      <v-btn @click="register" v-else class="mr-2">
        <span>Register</span>
      </v-btn>
      <v-btn @click="loginAndLogout">
        <span v-if="isAuthenticated" class="mr-2">Logout</span>
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
      username: this.$session.get('username'),
      logo: require('./assets/static/logo.png')
    };
  },

  methods:{
    home() {
      this.$router.push("/home")
    },
    loginAndLogout(){
      if(this.isAuthenticated){
        this.$session.destroy();
        this.isAuthenticated = false;
      } else {
        this.$router.push(`/login`);
      }
    },
    register() {
      this.$router.push("/register")
    }
  }
};
</script>
