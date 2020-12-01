<template lang="html">
      <div class="group">
        <b-row class="justify-content-center pb-1"><font-awesome-icon :icon="['fas', 'users']" /></b-row>
        <b-row class="justify-content-center"><p class="text-center mb-0">{{group}}</p></b-row>
       </div>
</template>

<script>
export default {
  props:{
    group: {
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
