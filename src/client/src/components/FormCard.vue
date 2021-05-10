<template>
  <v-row justify="space-around">
    <v-card width="1000" eleveation="24">
      <v-img
        height="250"
        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
      ></v-img>

      <v-row width="50">
        <v-text-field v-model="username" label="username" required>
        </v-text-field>
      </v-row>
      <v-row width="50">
        <v-text-field
          v-model="password"
          label="password"
          required
        ></v-text-field>
      </v-row>

      <v-app-bar flat color="rgba(0, 0, 0, 0)">
        <v-toolbar-title class="title white--text pl-0">
          Messages
        </v-toolbar-title>

        <v-spacer></v-spacer>
      </v-app-bar>

      <v-card-title class="white--text mt-8">
        <v-avatar size="56">
          <img
            alt="user"
            src="https://cdn.pixabay.com/photo/2020/06/24/19/12/cabbage-5337431_1280.jpg"
          />
        </v-avatar>
        <p class="ml-3">
          John Doe
        </p>
      </v-card-title>


        <v-timeline align-top dense>
          <v-timeline-item
            v-for="message in messages"
            :key="message.time"
            :color="message.color"
            small
          >
            <div>
              <div class="font-weight-normal">
                <strong>{{ message.from }}</strong> @{{ message.time }}
              </div>
              <div>{{ message.message }}</div>
            </div>
          </v-timeline-item>
        </v-timeline>
    </v-card>
  </v-row>
</template>
