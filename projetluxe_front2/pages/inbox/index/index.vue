<template lang="html">
  <section>
    <div v-for="mail in inbox" v-bind:key="mail.id" class="container-fluid px-0 ">
      <b-button class="link p-0 m-0 w-100" @click="display(mail)" disabled>
        <MailPreview
        :from="mail.from"
        :title="mail.topic"
        :preview="mail.content"/>
      </b-button>
    </div>
  </section>
</template>

<script>
import MailPreview from '~/components/MailPreview.vue'
export default {
  components:{
    MailPreview
  },
  computed: {
    inbox() {
      return this.$store.state.mailStore.inbox
    }
  },
  methods:{
    display(mail){
      console.log(mail);
    }
  }
}
</script>

<style lang="css" scoped>
.container-fluid{
  border-bottom: 1px solid #C9C9C9;
}
.link{
  color: black;
  background-color:white;
  border-color:white;
}

.link:hover,
.link:active:focus {
  color: black;
  background-color: white;
  border: 1px solid white;
}
</style>
