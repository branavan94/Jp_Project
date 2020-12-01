<template lang="html">
  <section>
    <MailForm :mailId="draft"/>
  </section>
</template>

<script>
import MailForm from '~/components/MailForm.vue'
import Header from '~/components/Header.vue'
export default {
  components:{
    MailForm,
    Header
  },
  computed:{
    draft() {
      return this.$store.state.mailStore.draftToModify
    }
  }
}
</script>

<style lang="css" scoped>
</style>
