<template>
<v-card class="transparent" flat>
  <v-list-item three-line >
  <!-- <v-card> -->
    <v-list-item-content>
      <v-list-item-title>{{author}}</v-list-item-title>
      <v-list-item-subtitle>
        {{contents}}
      </v-list-item-subtitle>
      <v-btn
        text
        small
        class="justify-start"
        :ripple="false"
        @click="showReplyForm = !showReplyForm"
        >Reply
      </v-btn>
      <v-text-field
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
        class="justify-start"
        :ripple="false"
        @click="showReplies = !showReplies"
        >Show {{replies.length}} Replies
      </v-btn>
      <div v-show="showReplies" v-for="reply in replies" :key="reply">
        <reply :author="reply.username" :contents="reply.content"></reply>
      </div>

    </v-list-item-content>
  <!-- </v-card> -->
  </v-list-item>
</v-card>
</template>


<script>
  import axios from 'axios';
  import Reply from "../components/Reply.vue"

  axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
  axios.defaults.xsrfCookieName = "XCSRF-TOKEN";
  
  export default {
    name: 'Comment',
    components: {
      'reply': Reply
    },
    props: ["id", "author", "contents", "replies"],
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

