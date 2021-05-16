<template>
<v-card class="transparent" flat>
  <v-list-item three-line >
    <v-list-item-content>
      <v-list-item-title>{{author}}</v-list-item-title>
      <v-list-item-subtitle>1/12/2921 This is dummy date</v-list-item-subtitle>
      <v-list-item-subtitle>
        {{content}}
      </v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</v-card>
  
</template>

<script>
  export default {
    props: ["author", "date", "content"]
  }
</script>

