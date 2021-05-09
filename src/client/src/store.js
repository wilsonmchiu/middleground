import Vue from 'vue';
const store = {
  state: Vue.observable({
    titles: [1, 2, 3]
  }),
  addNumber(newNumber) {
    this.state.numbers.push(newNumber);
  }
};

export default store;