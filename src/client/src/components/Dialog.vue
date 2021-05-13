<template>
  <div id="app">
    <v-app id="inspire">
      <div class="text-center">
        <v-dialog v-model="dialog" width="500">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">
              Click Me
            </v-btn>
          </template>

          <v-card>
            <v-card-title class="headline grey lighten-2">
              Logout
            </v-card-title>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="red" text @click="dialog = false">
                Cancel
              </v-btn>
              <v-btn color="primary" text @click="confirmLogout">
                Logout
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </v-app>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialog: true,
    };
  },
  methods: {
    confirmLogout() {
      this.dialog = false;
      this.$emit("confirmed-logout", true);
    },
  },
};
</script>
