<template>
<v-card color="rgb(211, 211, 211, 0)" class="my-n4" flat>
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
    color="blue darken-2"
    class="justify-start px-6 ml-4 mt-n6"
    :ripple="false"
    @click="showReplyForm = !showReplyForm"
    >Reply
  </v-btn>
  <v-text-field
    class="px-6"
    v-model="replyForm"
    :placeholder="replyForm"
    v-show="showReplyForm"
    :counter="160"
    :maxlength=160
    label="Write Comment Here"
    @keydown.enter="postReply(id)"
  ></v-text-field>

  <v-btn
    text
    small
    v-if="currentUser == author"
    color="blue darken-2"
    class="justify-start px-6 mt-n6"
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

  <v-btn
    text
    small
    color="blue darken-2"
    class="justify-start px-6 mt-n6"
    v-if="replies.length > 0"
    :ripple="false"
    @click="showReplies = !showReplies"
    >▾ Show {{replies.length}} Replies
  </v-btn>
  <div class="pl-6" v-show="showReplies" v-for="reply in replies" :key="reply">
    <reply :author="reply.username" :date="reply.date" :content="reply.content"></reply>
  </div>
</v-card>
</template>


<script>
  import axios from 'axios';
  import Reply from "../components/Reply.vue"
  
  export default {
    name: 'Comment',
    components: {
      'reply': Reply
    },
    props: ["id", "author", "date", "content", "replies"],
    data: function(){
      return{
        isAuthenticated : this.$session.exists(),
        currentUser: this.$session.get('username'),
        showReplyForm: false,
        showReplies: false,
        replyForm: "",
        apiRoot: process.env.VUE_APP_API_ROOT,
      };
    },
    methods: {
      replyCount(replies) {
        console.log(replies);
      },
      postReply(commentID) {
        const path = `http://${this.apiRoot}/replies/post_reply`;
        const payload = {
          username: this.currentUser,
          commentID: commentID,
          userReply: this.replyForm,
        };
        console.log(payload);
        if (this.isAuthenticated === false) {
          this.$router.push("/login");
        }
        else if (this.replyForm != "") {
          axios
          .post(path, payload)
          .then((response) => {
            console.log(response);
            window.location.reload();
          })
          .catch((error) => {
            console.log(error);
          });
        }
        this.replyForm = "";
      },
    },
    // beforeMount(){
    //   this.getReplies()
    // },
  }
</script>

