<template lang="html">
      <div class="arrival">
        <b-row class="justify-content-center  pb-1"><font-awesome-icon :icon="['fas', 'plane-arrival']" /></b-row>
        <b-row class="justify-content-center"><p class="text-center mb-0">{{arrival}}</p></b-row>
       </div>
</template>

<script>
export default {
  props:{
    arrival: {
      type:String,
      required:true
      }
    }
}
</script>

<style lang="css" scoped>
</style>

<style scoped>

</style>
