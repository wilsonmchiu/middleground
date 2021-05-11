<style>
  .v-card__text, .v-card__title {
    word-break: normal; /* maybe !important  */
  }
</style>

<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12" sm = "12" md="8" lg="8">
        <v-row>
          <v-card-text>
            <h1>{{articleData.title}}</h1>
            <br>
            <subtitle-1>By {{articleData.author}}</subtitle-1>      <br>
            <subtitle-1>{{articleData.timestamp}}</subtitle-1>
          </v-card-text>
          
          <v-img 
            :aspect-ratio="5/1"
            :src="articleData.image">
          </v-img>
          <v-card-text>
            {{articleData.body}}
          </v-card-text>
        </v-row>
          <v-card-text>
            <h1>Middle Ground </h1>
            <subtitle-1>{{comments.length}} comments</subtitle-1>
            <div v-for ="comment in comments" :key="comment" class="mb-5">
              <v-list-item three-line>
                <v-list-item-avatar size ="40" class = "mt-0"><v-img :src = "comments.avatar"></v-img></v-list-item-avatar>
                <v-list-item-title>{{comments.author}}</v-list-item-title>
                <v-list-item-subtitle>{{comments.content}}</v-list-item-subtitle>
              </v-list-item>
            </div>
          </v-card-text>
        <v-row>

        </v-row>
      </v-col>

      <v-col cols="12" sm= "12" md="4" lg="4">
        <hr class="grey--text" />
        <h4 class="mb-3 mt-3">What People Think</h4>
        <v-img 
          :aspect-ratio="5/1"
          src="https://canvasjs.com/wp-content/uploads/images/gallery/javascript-charts/overview/javascript-charts-graphs-index-data-label.png"></v-img>
        <h4 class="mb-3 mt-3">Related</h4>

        <div v-for="card in relatedCards" :key="card" class="mb-5">
          <v-skeleton-loader
            class="mx-auto"
            type="list-item-avatar-three-line"
            :loading="loading"
            tile
            large
          >
            <v-card class="card" tile flat>
              <v-row no-gutters>
                <v-col class="mx-auto" cols="3" sm="3" md="5" lg="5">
                  <!-- <v-responsive max-height="100%"> -->
                  <v-img
                    class="align-center"
                    :src="card.image"
                  >
                  </v-img>
                  <!-- </v-responsive> -->
                </v-col>
                <v-col>
                  <div class="ml-2">
                    <v-card-title
                      class="pl-2 pt-0 subtitle-1 font-weight-bold"
                      style="line-height: 1"
                    >
                      {{card.title}}
                    </v-card-title>

                    <v-card-subtitle
                      class="pl-2 pt-2 pb-0"
                      style="line-height: 1"
                    >
                      {{card.author}}<br />
                      {{card.timestamp}}
                    </v-card-subtitle>
                  </div>
                </v-col>
              </v-row>
            </v-card>
          </v-skeleton-loader>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  // import axios from 'axios';

  export default {
    data() {
      return {
        articleData: [],
        comments: [],
        relatedCards: []
      }
    },

    created(){
      this.articleData = {
        "title": "Local Green Man Rides Donkey Through London",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp",
        "body": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, \n\nconsectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered \n\n\n\n the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical \n\nLatin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of \n\nclassical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32."
      }

      this.comments = [
        {
        "author": "John Doe",
        "content": "i like apples",
        "avatar": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },
        {
        "author": "John Doe",
        "content": "i like pears",
        "avatar": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        }
      ]

      this.relatedCards = [
        {
        "title": "Local Green Man Rides Donkey Through London pt 1",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },
        {
        "title": "Local Green Man Rides Donkey Through London pt 2",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },
        {
        "title": "Local Green Man Rides Donkey Through London pt 3",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },        
        {
        "title": "Local Green Man Rides Donkey Through London pt 4",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },
        {
        "title": "Local Green Man Rides Donkey Through London pt 5",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },
        {
        "title": "Local Green Man Rides Donkey Through London pt 6",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },
        {
        "title": "Local Green Man Rides Donkey Through London pt 7",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },
        {
        "title": "Local Green Man Rides Donkey Through London pt 8",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },
        {
        "title": "Local Green Man Rides Donkey Through London pt 9",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        },
        {
        "title": "Local Green Man Rides Donkey Through London pt 10",
        "author": "John Doe",
        "timestamp": "1:32 PM PST, Sun June 13, 2001",
        "image": "https://i.insider.com/5c5dd439dde867479d106cc2?width=1000&format=jpeg&auto=webp"
        }
      ]
    }

    // // Fetches posts when the component is created.
    // created() {
    //   axios.get(`http://jsonplaceholder.typicode.com/posts`)
    //   .then(response => {
    //     // JSON responses are automatically parsed.
    //     this.articleData = response.data
    //   })
    // }
  }
</script>