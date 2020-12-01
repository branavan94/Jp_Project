<template lang="html">
      <div class="group">
        <b-row class="cat justify-content-center pb-1"><font-awesome-icon :icon="icon" /></b-row>
        <b-row class="justify-content-center"><p class="text-center mb-0">{{group}}</p></b-row>
       </div>
</template>

<script>
export default {
  props:{
    group: {
      type:String,
      required:true
    },
    icon:{
      type: Array,
      required:true
    }
}
}
</script>

<style lang="css" scoped>
</style>

<style scoped>
.cat{
  color:#FFD400;
}
</style>
