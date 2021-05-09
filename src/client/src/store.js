import Vue from 'vue';

export const store = {
  state: Vue.observable({
    articles: [],
  }),
  setArticles: function(articles) {
    Object.assign(this.state.articles, articles);
  },
};
