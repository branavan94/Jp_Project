import vuex from 'vuex';


/*This is the data, what we want to conserve*/
export const state = () => {
  users: [];
  userLogged:{};
}


/*Here the functions we want to commit*/
export const mutations = {
  setUser(state, user) {
    state.users = user ;
  },
  setUserLogged(state, user){
    state.userLogged = user ;
  }
}
