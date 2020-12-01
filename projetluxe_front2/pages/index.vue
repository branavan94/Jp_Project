<template>
  <section>
    <Header :logged="logged" :loginpage="false"/>
    <div>
      <b-jumbotron id="home-1st-section" fluid>
        <div class="container">
          <h1></h1>
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
 
  computed:{
    logged(){
      if(this.$store.state.userStore.userLogged && this.$store.state.userStore.userLogged!={})
      {
        return true;
      }
      else{
        return false
      }
    }
  }
}
</script>

<style>
#home-1st-section{
  width: 100%;
  height: 100%;
  height: 85vh;
  padding-bottom:0;
  margin-bottom:0;
  background:url('../assets/background-1bis.jpg');
  background-position: center bottom;
  background-repeat: no-repeat ;
  background-size: cover;
  overflow: hidden;
}

#home-1st-section img{
  display:absolute;
  opacity:0.4;
}

.container{
  opacity:1;
}
</style>
