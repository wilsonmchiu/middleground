import Vue from 'vue';
import App from './App.vue';
import VueSession from 'vue-session'
import vuetify from './plugins/vuetify';
import router from './router';

Vue.config.productionTip = false;
Vue.use(VueSession)

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

