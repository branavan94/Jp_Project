<template lang="html">
      <div class="name">
        <b-row class="justify-content-center pb-1"><font-awesome-icon :icon="['fas', 'user']" /></b-row>
        <b-row class="justify-content-center"><p class="text-center mb-0">{{name}}</p></b-row>
      </div>
</template>

<script>
export default {
  props:{
    name: {
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
