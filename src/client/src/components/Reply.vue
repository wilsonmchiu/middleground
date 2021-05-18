<template>
<v-card class="transparent my-n4" flat>
  <v-list-item three-line >
    <v-list-item-content>
      <v-list-item-title>{{author}}</v-list-item-title>
      <v-list-item-subtitle>{{date}}</v-list-item-subtitle>
      <v-list-item-subtitle>
        {{content}}
      </v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>

  <v-btn
    text
    small
    v-if="currentUser == author"
    color="blue darken-2"
    class="justify-start px-6 ml-4 mt-n6"
    :ripple="false"
    >Edit
  </v-btn>

  <v-btn
    text
    small
    v-if="currentUser == author"
    color="red darken-4"
    class="justify-start px-6 mt-n6"
    :ripple="false"
    >Delete
  </v-btn>
</v-card>
  
</template>

<script>
  export default {
    props: ["author", "date", "content"],
    data: function(){
      return{
        currentUser: this.$session.get('username')
      };
    }
  }
</script>