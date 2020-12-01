<template>
  <!-- HEADER DISPLAY WHEN USER LOGGED-->
  <div v-if="logged && !loginpage">
    <!-- to make the bar stick to the window : fixed="top"   -->
    <b-navbar toggleable="lg" variant="faded" type="light" class="shadow-sm" id="navbar">
      <b-navbar-toggle target="nav-collapse1"></b-navbar-toggle>
      <b-collapse id="nav-collapse1" is-nav>

        <b-navbar-nav class="col-sm-4">
          <b-nav-item ><nuxt-link class="pages" to="/concierge">ACCUEIL</nuxt-link></b-nav-item>
          <b-nav-item><nuxt-link class="pages" to="/clients">MES CLIENTS</nuxt-link></b-nav-item>
          <b-nav-item class="pages"><nuxt-link class="pages" to="/inbox">MA MESSAGERIE</nuxt-link></b-nav-item>
        </b-navbar-nav>

        <b-navbar-brand class="d-inline-block col-sm-4 align-center" href="/">
          <b-container text-align:center>
            <b-row no-gutters>
              <b-img src="~/assets/logoJP.png" alt="LogoJP" height=50 center></b-img>
            </b-row>
            <p class="titlePL">FW Manager</p>
          </b-container>
        </b-navbar-brand>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto" >
          <b-nav-item-dropdown text="LANGUE" right>
            <b-dropdown-item href="#">FR</b-dropdown-item>
            <b-dropdown-item href="#" disabled>EN</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item href="#" class="pages" disabled right>AIDE</b-nav-item>
          <b-nav-item href="#" @click="logout" class="pages" right>SE DECONNECTER</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
  </b-navbar>
  </div>

<!-- HEADER DISPLAY WHEN USER NOT LOGGED AND ON THE LOGIN PAGE-->
  <div v-else-if="!logged && loginpage">
    <!-- to make the bar stick to the window :  fixed="top" -->
    <b-navbar toggleable="lg" variant="faded" type="light" class="d-block shadow-sm" id="navbar">
      <b-navbar-toggle target="nav-collapse2"></b-navbar-toggle>

    <b-collapse id="nav-collapse2" is-nav>
        <b-navbar-nav class="col-sm-4">
            <!--<font-awesome-icon :icon="['fas', 'arrow-left']" class="align-self-center m-2"/>-->
            <b-nav-item href="/">
              <font-awesome-icon :icon="['fas', 'arrow-left']" class="align-middle m-2"/>
              <b-nav-text class="align-middle">RETOUR A L'ACCUEIL</b-nav-text>
            </b-nav-item>
        </b-navbar-nav>
        <b-navbar-brand class="d-inline-block col-sm-4 align-center" href="/">
          <b-container text-align:center>
            <b-row no-gutters>
              <b-img src="~/assets/logoJP.png" alt="LogoJP" height=50 center></b-img>
            </b-row>
            <p class="titlePL">FW Manager</p>
          </b-container>
        </b-navbar-brand>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto" >
          <b-nav-item-dropdown text="LANGUE" right>
            <b-dropdown-item href="#">FR</b-dropdown-item>
            <b-dropdown-item href="#" disabled>EN</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item href="#" class="pages" disabled right>CONTACT</b-nav-item>
        </b-navbar-nav>
      </b-collapse>



    </b-navbar>
  </div>

<!-- HEADER DISPLAY WHEN USER NOT LOGGED AND NOT ON THE LOGIN PAGE-->

  <div v-else>
    <!-- to make the bar stick to the window :  fixed="top" -->
    <b-navbar toggleable="lg" variant="faded" type="light" class="shadow-sm" id="navbar">
    <b-navbar-toggle target="nav-collapse3"></b-navbar-toggle>
    <b-collapse id="nav-collapse3" is-nav>

        <b-navbar-nav class="col-sm-4">
          <b-nav-item href="/" class="pages">ACCUEIL</b-nav-item>
          <b-nav-item href="https://www.johnpaul.com/fr/accueil/" class="pages">JOHN PAUL</b-nav-item>
        </b-navbar-nav>

        <b-navbar-brand class="d-inline-block col-sm-4 align-center" href="/">
          <b-container text-align:center>
            <b-row no-gutters>
              <b-img src="~/assets/logoJP.png" alt="LogoJP" height=50 center></b-img>
            </b-row>
            <p class="titlePL">FW Manager</p>
          </b-container>
        </b-navbar-brand>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown class="pages" text="LANGUE" right>
            <b-dropdown-item href="#">FR</b-dropdown-item>
            <b-dropdown-item href="#" disabled>EN</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item href="/login" class="pages">SE CONNECTER</b-nav-item>
          <b-nav-item  class="pages" disabled right>CONTACT</b-nav-item>
        </b-navbar-nav>
      </b-collapse>

    </b-navbar>
  </div>
</template>
<script type="text/javascript">

export default {
  props: {
    loginpage:{
        type: Boolean,
        required: false,
        default:false
      },
      logged:{
          type: Boolean,
          required: false,
          default: true
        }
    },
  methods: {
    logout(){
      this.$store.commit('userStore/setUserLogged', {});
      window.location.href="/"

    }
  }
}
</script>
<style scoped>
.pages{
  color:#C9C9C9;
}
.titlePL{
  color:#FFD400;
  font-size: 20px;
  text-align: center;
  margin: 0;

}
.nav-brand{
  text-align: center;
}
.left-arrow
{
  max-width: 40px;
}
#navbar{
  background-color: white;
}
</style>
