<template lang="html">
      <div class="phone">
        <b-row class="justify-content-center  pb-1"><font-awesome-icon :icon="['fas', 'mobile-alt']" /></b-row>
        <b-row class="justify-content-center"><p class="text-center mb-0">{{phone}}</p></b-row>
       </div>
</template>

<script>
export default {
  props:{
    phone: {
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
