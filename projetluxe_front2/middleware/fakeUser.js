import axios from 'axios';

export default function({store}){
  var user1 = {
    id: "Lindsay",
    key: "ESILV2019",
    status: "concierge"
  }
  var user2 = {
    id: "Diane",
    key: "ProjetLuxe",
    status: "concierge"
  }
  var user3 = {
    id: "Nicolas",
    key: "JPProject",
    status: "concierge"
  }
  store.commit('userStore/setUser', [user1, user2, user3]);
}
