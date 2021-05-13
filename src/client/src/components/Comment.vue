<template>
<v-card class="transparent" flat>
  <v-list-item three-line >
  <!-- <v-card> -->
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
        >Show {{replies.length}} Replies
      </v-btn>
      <div v-show="showReplies" v-for="reply in replies" :key="reply">
        <reply :author="reply.author" :contents="reply.contents" :avatar="reply.avatar"></reply>
      </div>


    </v-list-item-content>
  <!-- </v-card> -->
  </v-list-item>
</v-card>
  
</template>



<script>
  import Reply from "../components/Reply.vue"
  export default {
    name: 'Comment',
    components: {
      'reply': Reply
    },
    props: ["author", "contents", "avatar"],
    data: function(){
                return{
                    showReplyForm: false,
                    showReplies: false,
                    replies: []
                };
            },
    created(){
      this.replies = [
        {
        "author": "Adam Smith",
        "contents": "It is not from the benevolence of the butcher, the brewer, or the baker that we expect our dinner, but from their regard to their own interest. All money is a matter of belief",
        "avatar": "https://i.cbc.ca/1.5303387.1583953990!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_780/adam-smith-the-muir-portrait-circa-1800.jpg"
        },
        {
        "author": "George Washington",
        "contents": "It is better to offer no excuse than a bad one. It is better to be alone than in bad company. If freedom of speech is taken away, then dumb and silent we may be led, like sheep to the slaughter.",
        "avatar": "https://www.history.com/.image/ar_16:9%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_faces:center%2Cq_auto:good%2Cw_620/MTcwNDY1NDEzNzMyNDQzOTMy/wshington_timeline.jpg"
        }
      ]
    }
  }
</script>

