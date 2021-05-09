import Vue from 'vue';

export const store = {
  state: Vue.observable({
    articles: [],
  }),
  setArticles: function(articles) {
    //Object.assign(this.state.articles, articles);
    //this.state.articles = articles.splice(0, articles.length);
    this.state.articles = articles
    console.log("in store.js", this.state.articles)
    //this.state.articles.push(...articles);
  },
};