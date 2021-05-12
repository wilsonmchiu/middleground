import Vue from 'vue';

export const store = {
  state: Vue.observable({
    articles: [],
  }),
  setArticles: function(articles) {
    this.state.articles = articles;
    console.log('in store.js', this.state.articles);
  },
};
