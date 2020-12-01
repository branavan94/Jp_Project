<template>
  <v-app class="grey lighten-4">
    <NavSidebar />

    <v-content class="mx-4 mb-4">
      <nuxt/>
    </v-content>

  </v-app>
</template>

<script>
import NavSidebar from '~/components/NavSidebar'
export default {
  components: { NavSidebar },
  data () {
    return {

    }
  }
}
</script>
