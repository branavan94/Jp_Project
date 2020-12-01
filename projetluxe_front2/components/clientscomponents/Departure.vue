<template lang="html">
      <div class="departure">
        <b-row class="justify-content-center  pb-1"><font-awesome-icon :icon="['fas', 'plane-departure']" /></b-row>
        <b-row class="justify-content-center"><p class="text-center mb-0">{{departure}}</p></b-row>
       </div>
</template>

<script>
export default {
  props:{
    departure: {
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
