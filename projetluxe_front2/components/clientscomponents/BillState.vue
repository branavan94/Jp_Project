<template lang="html">
  <div v-if="state">
    <b-row class="justify-content-center" style="color: green;">
      <p class="text-center mb-0">Factures complètes</p>
    </b-row>
  </div>
  <div v-else>
    <b-row class="justify-content-center" style="color: red;">
      <p class="text-center mb-0">Facture(s) manquante(s)</p>
    </b-row>
  </div>
</template>

<script>
export default {
  props:{
    state: {
      state:Boolean,
      required:true
      }
    }
}
</script>

<style lang="css" scoped>
</style>

<style scoped>

</style>
