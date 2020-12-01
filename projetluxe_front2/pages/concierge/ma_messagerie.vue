<template>
  <v-app>

    <NavSidebar />
    <v-content></v-content>


  </v-app>
</template>

<script>

import NavSidebar from '~/components/NavSidebar.vue'

  export default {
  components: {
    NavSidebar
  },
  computed : {
    user () {
      return this.$store.state.userStore.userLogged
   }
 }
}
</script>
