<template>
  <v-card height="350px">
    <v-card-text>
      <h1>Article Name</h1>
      <h3>By Austhor</h3>
      <h3>Timestamp</h3>
    </v-card-text>
    
    <v-img 
      :aspect-ratio="5/1"
      src="https://picsum.photos/id/11/500/300"></v-img>

    <v-card-text>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
      It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
      Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
    </v-card-text>

    <v-navigation-drawer
      app
      floating
      right
    >
      <v-card-text>
        <h1>What People Think</h1>
      </v-card-text>
      <v-img 
        :aspect-ratio="5/1"
        src="https://canvasjs.com/wp-content/uploads/images/gallery/javascript-charts/overview/javascript-charts-graphs-index-data-label.png"></v-img>

      <v-card-text>
        <h1>Related</h1>
      </v-card-text>

      <v-card-text>
        Article 1
      </v-card-text>
      <v-img 
        :aspect-ratio="3/2"
        src="https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"></v-img>
      <v-card-text>
        Article 2
      </v-card-text>
      <v-img 
        :aspect-ratio="3/2"
        src="https://cdn.vox-cdn.com/thumbor/1i4ECs3zLWaWf32jmEFAc_U4AyI=/0x0:1920x1080/1200x800/filters:focal(807x387:1113x693)/cdn.vox-cdn.com/uploads/chorus_image/image/54014619/shrek.0.jpg"></v-img>
      <v-card-text>
        Article 3
      </v-card-text>
      <v-img 
        :aspect-ratio="3/2"
        src="https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"></v-img>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          { title: 'Home', icon: 'mdi-home-city' },
          { title: 'My Account', icon: 'mdi-account' },
          { title: 'Users', icon: 'mdi-account-group-outline' },
        ],
      }
    },
  }
</script>