/*export default function({store}){
    async asyncData({ $axios, params }) {
    try {
      let users = await this.$axios.get('/Concierge');
      store.commit('userStore/setUser', users);
      return { users };
    } catch (e) {
      return { users: [] };
    }
  }
    /*axios.$get('/Concierge/')
      .then((res)=>{
        store.commit('userStore/setUser', res);
      })
}
import axios from 'axios';

export default function ({ store }) {

  return axios.get('http://localhost:8000/api/Concierge')
    .then(response => {
      store.commit('userStore/setUser', response);
    })
    .catch((e) => {
      store.commit('userStore/setUser', []);
    })
}*/
