<style>
.author {
  font-family: Arial, Helvetica, sans-serif;
  color: #000000;
  font-weight: 500;
  padding-top: 0px;
  padding-bottom: 0px;
  display: inline;
  font-size: 18px;
}
.date {
  font-family: Arial, Helvetica, sans-serif;
  color: #909090;
  padding-top: 0px;
  padding-bottom: 0px;
  display: inline;
  font-size: 12px;
}
.content {
  font-family: Arial, Helvetica, sans-serif;
  color: #505050;
  padding-top: 0px;
  padding-bottom: 0px;
  display: inline;
  font-size: 15px;
}

</style>

<template>
  <v-card color="rgb(211, 211, 211, 0)" class="my-n0" flat>
    <div v-if="!showEditForm">
      <v-container>
        <v-row no-gutters >
            <v-list-item-avatar>
              <v-img max-height="150" :src="avatar"> </v-img>
            </v-list-item-avatar>
          <v-col align class="pa-2">
            <p class="author mr-2">{{ author }}</p>
            <p class="date">{{ date }}</p>
            <br />
            <p class="content md-2">{{ newContent }}</p>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <!-- Reply Button -->
    <v-btn
      v-if="!showEditForm & !showReplyForm"
      text
      small
      color="blue darken-2"
      class="justify-start px-6 ml-0 mt-n1"
      :ripple="false"
      @click="showReplyForm = !showReplyForm"
      >Reply
    </v-btn>

    <!-- Delete Button -->
    <v-btn
      v-if="deleteEditAllowed"
      text
      small
      color="red darken-4"
      class="justify-start px-6 mt-n1"
      :ripple="false"
      @click="deleteComment(id)"
      >Delete
    </v-btn>

    <!-- Edit Button -->
    <v-btn
      v-if="deleteEditAllowed"
      text
      small
      color="blue darken-4"
      class="justify-start px-6 mt-n1"
      :ripple="false"
      @click="showEditForm = !showEditForm"
      >Edit
    </v-btn>

    <!-- Reply Field -->
    <v-text-field
      class="px-6"
      v-model="replyForm"
      :placeholder="replyForm"
      v-show="showReplyForm"
      :counter="160"
      :maxlength="160"
      label="Write Reply Here"
      @keydown.enter="postReply(id); showReplyForm = false;"
    ></v-text-field>

    <!-- Post Reply Button -->
    <v-btn
      v-show="showReplyForm"
      text
      small
      color="blue darken-4"
      class="justify-start px-6 ml-4 mt-n6"
      :ripple="false"
      @click="
        postReply(id);
        showReplyForm = false;
      "
      >Post Reply
    </v-btn>

    <!-- Cancel Reply Button -->
    <v-btn
      v-show="showReplyForm"
      text
      small
      color="red darken-4"
      class="justify-start px-6 ml-4 mt-n6"
      :ripple="false"
      @click="showReplyForm = false"
      >Cancel
    </v-btn>

    <!-- Edit Comment Field -->
    <v-text-field
      class="pl-4 pr-6 pt-2"
      v-model="newContent"
      v-show="showEditForm"
      :counter="160"
      :maxlength="160"
      :label="'Edit your comment from ' + date"
      @keydown.enter="editComment(id); showEditForm = !showEditForm;"
    ></v-text-field>

    <!-- Save Edit Button -->
    <v-btn
      v-show="showEditForm"
      text
      small
      color="blue darken-4"
      class="justify-start px-6 ml-4 mt-n1"
      :ripple="false"
      @click="
        editComment(id);
        showEditForm = !showEditForm;
      "
      >Save
    </v-btn>

    <!-- Cancel Edit Button -->
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

    <br v-if="showReplyForm" />

    <!-- Show Replies Button -->
    <v-btn
      text
      small
      color="blue darken-2"
      class="justify-start px-6 mt-n1"
      v-if="replies != undefined && replies.length > 0"
      :ripple="false"
      @click="showReplies = !showReplies"
      >▾ Show {{ replies.length }} Replies
    </v-btn>

    <div
      class="pl-6"
      v-show="showReplies"
      v-for="reply in replies"
      :key="reply.id"
    >
      <reply
        @deleteReply="deleteReply"
        :author="reply.username"
        :date="reply.date"
        :content="reply.content"
        :id="reply.id"
      ></reply>
    </div>
  </v-card>
</template>


<script>
import axios from "axios";
import Reply from "../components/Reply.vue";

export default {
  name: "Comment",
  components: {
    reply: Reply,
  },
  props: ["id", "author", "date", "content"],
  emits: ["deleteComment"],
  data: function () {
    return {
      isAuthenticated: this.$session.exists(),
      currentUser: this.$session.get("username"),
      showReplyForm: false,
      showEditForm: false,
      showReplies: false,
      replyForm: "",
      apiRoot: process.env.VUE_APP_API_ROOT,
      newContent: this.content,
      avatar:
        "https://cdn2.iconfinder.com/data/icons/facebook-51/32/FACEBOOK_LINE-01-512.png",
      replies: []
    };
  },
  created() {
    this.getReplies();
  },
  methods: {
    deleteReply(replyID) {
      this.replies = this.replies.filter((item) => item.id != replyID);
    },
    getReplies() {
      const path = `${this.apiRoot}/replies/get`;
      axios
        .get(path, {
          params: {
            commentID: this.id,
          },
        })
        .then((response) => {
          this.replies = response.data.replies;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    postReply(commentID) {
      const path = `${this.apiRoot}/replies/post`;
      const payload = {
        username: this.currentUser,
        commentID: commentID,
        userReply: this.replyForm,
      };
      console.log(payload);
      if (this.isAuthenticated === false) {
        this.$router.push("/login");
      } else if (this.replyForm != "") {
        axios
          .post(path, payload)
          .then((response) => {
            this.replies.push(response.data.newReply);
          })
          .catch((error) => {
            console.log(error);
          });
      }
      this.replyForm = "";
    },
    deleteComment(commentID) {
      const path = `${this.apiRoot}/comments/delete`;
      const payload = {
        commentID: commentID,
      };
      console.log(payload);
      if (this.isAuthenticated === false) {
        this.$router.push("/login");
      }
      axios
        .put(path, payload)
        .then((response) => {
          console.log(response);
          this.$emit("deleteComment", commentID);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editComment(commentID) {
      const path = `${this.apiRoot}/comments/edit`;
      const payload = {
        commentID: commentID,
        content: this.newContent,
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
  computed: {
    deleteEditAllowed: function () {
      return (
        this.currentUser == this.author &&
        !this.showEditForm &&
        !this.showReplyForm
      );
    },
  },
};
</script>

