import Vue from 'vue';

export const store = {
  state: Vue.observable({
    articles: [],
    isAuthenticated: false,
    username: null,
  }),
  setArticles: function(articles) {
    this.state.articles = articles;
    console.log('in store.js', this.state.articles);
  },
  login: function(username) {
    this.state.username = username;
    this.state.isAuthenticated = true;
  },
  logout: function() {
    this.state.username = null;
    this.state.isAuthenticated = false;
  },
};
