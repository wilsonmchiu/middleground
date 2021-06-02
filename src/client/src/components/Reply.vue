<template>
<v-card class="transparent my-n0" flat>
  <div v-if="!showEditForm">
    <v-list-item-avatar>
      <v-img :src="avatar"></v-img>
    </v-list-item-avatar>
    <p class="author mr-2">{{author}}</p>
    <p class="date">{{date}}</p><br/>
    <p class="content ml-4">{{content}}</p><br/>
  </div>

  <v-btn
    text
    small
    v-if="deleteEditAllowed"
    color="red darken-4"
    class="justify-start px-6 ml-4 mt-n1"
    :ripple="false"
    @click="deleteReply(id)"
    >Delete
  </v-btn>

  <v-btn
    text
    small
    v-if="deleteEditAllowed"
    color="blue darken-4"
    class="justify-start px-6 ml-4 mt-n1"
    :ripple="false"
    @click="showEditForm = !showEditForm"
    >Edit
  </v-btn>

  <v-text-field
    class="pl-4 pr-6 pt-6"
    v-model="newContent"
    v-show="showEditForm"
    :counter="160"
    :maxlength=160
    :label="'Edit your reply from ' + date"
    @keydown.enter="editReply(id)"
  ></v-text-field>
  
  <!-- Save Edit Button -->
  <v-btn
    v-show="showEditForm"
    text
    small
    color="blue darken-4"
    class="justify-start px-6 ml-4 mt-n1"
    :ripple="false"
    @click="editReply(id); showEditForm = !showEditForm"
    >Save
  </v-btn>
  <v-btn
    v-show="showEditForm"
    text
    small
    color="blue darken-4"
    class="justify-start px-6 ml-4 mt-n1"
    :ripple="false"
    @click="showEditForm = !showEditForm"
    >Cancel
  </v-btn>
</v-card>
  
</template>

<script>
import axios from 'axios';
  export default {
    props: ["author", "date", "content", "id"],
    emits: ['deleteReply'],
    data: function(){
      return{
        currentUser: this.$session.get('username'),
        showEditForm: false,
        apiRoot: process.env.VUE_APP_API_ROOT,
        avatar: "https://cdn2.iconfinder.com/data/icons/facebook-51/32/FACEBOOK_LINE-01-512.png"
      };
    },
    methods:{
      deleteReply(replyID) {
        const path = `${this.apiRoot}/replies/delete`;
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
          this.$emit('deleteReply', replyID)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editReply(replyID) {
        const path = `${this.apiRoot}/replies/edit`;
        const payload = {
          replyID: replyID,
          content: this.newContent
        };
        console.log(payload);
        if (this.isAuthenticated === false) {
          this.$router.push("/login");
        }
        axios
        .put(path, payload)
        .then((response) => {
          console.log(response);
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