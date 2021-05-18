<template>
<v-card class="transparent my-n4" flat>
  <v-list-item three-line v-if="!showEditForm">
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
    v-if="deleteEditAllowed"
    color="red darken-4"
    class="justify-start px-6 ml-4 mt-n6"
    :ripple="false"
    @click="deleteReply(id)"
    >Delete
  </v-btn>

  <v-btn
    text
    small
    v-if="deleteEditAllowed"
    color="blue darken-4"
    class="justify-start px-6 ml-4 mt-n6"
    :ripple="false"
    @click="showEditForm = !showEditForm"
    >Edit
  </v-btn>

  <v-text-field
    class="pl-6 pr-6"
    v-model="content"
    v-show="showEditForm"
    :counter="160"
    :maxlength=160
    :label="'Edit your reply from ' + date"
    @keydown.enter="editReply(id)"
  ></v-text-field>
</v-card>
  
</template>

<script>
import axios from 'axios';
  export default {
    props: ["author", "date", "content", "id"],
    data: function(){
      return{
        currentUser: this.$session.get('username'),
        showEditForm: false,
        apiRoot: process.env.VUE_APP_API_ROOT,
      };
    },
    methods:{
      deleteReply(replyID) {
        const path = `http://${this.apiRoot}/replies/delete`;
        const payload = {
          replyID: replyID
        };
        console.log(payload);
        if (this.isAuthenticated === false) {
          this.$router.push("/login");
        }
        axios
        .put(path, payload)
        .then((response) => {
          console.log(response);
          window.location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
        
    },
    editReply(replyID) {
        const path = `http://${this.apiRoot}/replies/edit`;
        const payload = {
          replyID: replyID,
          content: this.content
        };
        console.log(payload);
        if (this.isAuthenticated === false) {
          this.$router.push("/login");
        }
        axios
        .put(path, payload)
        .then((response) => {
          console.log(response);
          window.location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
        
    },
  },
  computed:{
      deleteEditAllowed: function(){
          return this.currentUser==this.author && !this.showEditForm
      } 
  }
}
</script>