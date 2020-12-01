<template>
  <section>
    <Header :logged="false" :loginpage="true"/>
    <div>
    <b-jumbotron id="login-form-section" fluid >
      <!--<b-img src="~/assets/background.jpg" alt="background" center fluid></b-img>-->
      <div class="container  align-middle justify-content-center">
        <b-card
          id="login-form"
          text-variant="white"
          header="BIENVENUE"
          header-tag="header"
          class="my-auto mx-auto text-center"
          style="max-width: 540px;">
          <b-form @submit="onSubmit">
            <b-form-group
            id="id-field"
            label-cols-sm="4"
            label="Identifiant"
            label-for="id-input">
              <b-form-input id="id-input"
              class="rounded-lg"
              v-model="form.id"
              placeholder="Identifiant" required trim></b-form-input>
            </b-form-group>

            <b-form-group
            id="securitykey-field"
            label-cols-sm="4"
            label="Clé de sécurité"
            label-for="securitykey-input"
            :invalid-feedback="invalidFeedback"
            :valid-feedback="validFeedback"
            :state="state">
              <b-form-input id="securitykey-input"
              type="password"
              placeholder="Clé de sécurité"
              class="rounded-lg"
              v-model="form.securitykey"
              :state="state" required trim></b-form-input>
            </b-form-group>
            <b-button class="login-button justify-content-center" type="submit"><p class="align-middle mb-0 my-1 mx-4">SE CONNECTER</p></b-button>
          </b-form>
        </b-card>
      </div>
    </b-jumbotron>
  </div>
  </section>
</template>

<script>
import Header from '~/components/Header.vue'

export default {
  components: {
    Header
  },

  async asyncData({ $axios, params }) {
    try {
      let data = await $axios.$get(`/Concierge/`);
      return { data };
    } catch (e) {
      return { data: [] };
    }
  },
  computed: {
    state() {
      if(this.form.securitykey.length == 0)
      {
        return null
      }
      else if(this.form.securitykey.length >= 4)
      {
        return true
      }
      else {
        return false
      }
    },
    invalidFeedback() {
      if (this.form.securitykey.length >= 8) {
        return ''
      } else if (this.form.securitykey.length > 0) {
        return 'Entrer au moins 4 caractères'
      } else {
        return 'Entrer une valeur'
      }
    },
    validFeedback() {
      return this.state === true ? 'Thank you' : ''
    }
  },
  data() {
    return {
      form: {
        id: '',
        securitykey:''},
      data:[]
    }
  },
  methods: {
      onSubmit(evt) {
        evt.preventDefault()
        const users = this.data
        console.log(users);
        var user = users.filter(e => e.login === this.form.id)
        console.log(user)
        if(user.length > 0 && user[0].mdp == this.form.securitykey )
        {
          var userLogged = user[0];
          this.$store.commit('userStore/setUserLogged', userLogged);
          console.log(this.$store.state.userStore.userLogged);
          this.$router.push({ path: "/concierge"});
        }
        else{
          alert(JSON.stringify(this.form) + "incorrect");

        }
      }
    }
}
</script>

<style scoped>
#login-form-section{
  width: 100%;
  height: 85vh;
  padding-bottom:0;
  margin-bottom:0;
  background:url('../assets/background-login.jpeg');
  background-repeat: no-repeat ;
  background-size: cover;
  background-position: center;
}
#login-form{
  background-color: rgba(0, 0, 0, .5);
}
.login-button
{
  border-radius: 10px;
  border-color:black;
  color:#FFD400;
  background-color: black;
}
.login-button:hover
{
  border-color:black;
  color: yellow;
  background-color: black;
}
</style>
