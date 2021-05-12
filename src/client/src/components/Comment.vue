<template>
<v-card class="transparent" flat>
  <v-list-item three-line >
    <v-list-item-avatar>
      <v-img 
        :src="avatar">
      </v-img>
    </v-list-item-avatar>

    <v-list-item-content>
      <v-list-item-title>{{author}}</v-list-item-title>
      <v-list-item-subtitle>
        {{contents}}
      </v-list-item-subtitle>
          <v-btn
            text
            small
            :ripple="false"
            @click="showReplyForm = !showReplyForm"
            >Reply
          </v-btn>
          <v-text-field
            v-show="showReplyForm"
            :counter="160"
            label="Write Comment Here"
          ></v-text-field>

          <v-btn
            text
            small
            :ripple="false"
            @click="showReplies = !showReplies"
            >Show Replies
          </v-btn>
          <h1 v-show="showReplies">Placeholder for replies component</h1>

    </v-list-item-content>
  </v-list-item>
</v-card>
  
</template>

<script>
  export default {
    props: ["author", "contents", "avatar"],
    data: function(){
                return{
                    showReplyForm: false,
                    showReplies: false
                }
            }
    };
</script>

