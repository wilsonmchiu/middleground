<template>
<v-card class="transparent" flat>
  <v-list-item three-line >
    <v-list-item-content>
      <v-list-item-title>{{author}}</v-list-item-title>
      <v-list-item-subtitle>
        {{contents}}
      </v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</v-card>
  
</template>

<script>
  export default {
    props: ["author", "contents"]
  }
</script>

