<template lang="html">
  <section class="back w-100">
    <div class="m-4">
    <NuxtChild :key="$route.params"/>
    </div>
  </section>
</template>

<script>
import MailForm from '~/components/MailForm.vue'
import Header from '~/components/Header.vue'
  export default {
    layout: 'nav',
  components:{
    MailForm,
    Header
  }
}
</script>

<style lang="css" scoped>
.back{
  background-color:#F7F7F7;
  height: 100vh;

}
</style>
