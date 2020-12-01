<template lang="html">
  <div class="back">
    <b-badge class="new-mail w-100"><p class = "mb-0 my-2 w-100 py-auto align-middle">Nouveau message</p></b-badge>
    <form class="new-mail-form" v-on:submit.prevent="onSave()">
      <AppControlInput v-model="mailDraft.from">Expéditeur</AppControlInput>

      <AppControlInput v-model="mailDraft.to">Destinataire</AppControlInput>

      <AppControlInput v-model="mailDraft.topic">Sujet</AppControlInput>

      <AppControlInput
                control-type="textarea"
                v-model="mailDraft.content">Mail</AppControlInput>

      <AppButton type="submit">Envoyer</AppButton>

      <AppButton
                type="button"
                style="margin-left: 10px"
                btn-style="cancel"
                @click="onCancel">Annuler</AppButton>
    </form>
  </div>
</template>

<script>
import AppButton from '~/components/AppButton.vue';
import AppControlInput from '~/components/AppControlInput.vue';
  export default{
    props:{
      mailId:{
        type: Object,
        required:false
      }
    },
    components:{
      AppButton,
      AppControlInput
    },
    data(){
      return{
        mailDraft: this.mailId ? {...this.mailId}:{
          topic: '',
          to:'',
          from: this.$store.state.userStore.userLogged.name,
          content:''
        }
      }
    },
    methods:{
      onCancel(){
        this.$router.push("/inbox");
      },
      onSave(){
        //console.log(this.mailDraft);
        if(this.mailDraft.to && this.mailDraft.content)
        {
          if(!this.mailId)
          {
            const drafts = this.$store.state.mailStore.drafts
            var id = drafts.length + 1
            var newDraft = {
              id: id,
              topic:this.mailDraft.topic,
              to:this.mailDraft.to,
              from:this.mailDraft.from,
              content: this.mailDraft.content
            }
            this.$store.commit('mailStore/addDraft', newDraft);

            alert("Message non envoyé, voir les brouillons.");
            //console.log(this.$store.state.mailStore.drafts);
            this.$router.push("/inbox/drafts");
          }
          else{
            this.$store.commit('mailStore/modifyDraft', this.mailDraft);

            alert("Message non envoyé, voir les brouillons.");
            console.log(this.$store.state.mailStore.drafts);
            this.$router.push("/inbox/drafts");
          }
        }
      }
    }
  }
</script>

<style scoped>
.new-mail{
  background-color: #FFD400;
  border-radius: 10px 10px 0px 0px;
}
.new-mail-form{
  padding: 20px;
  background-color: white;
  border: 1px solid #C9C9C9;
  border-radius: 0px 0px 5px 5px;
}
</style>
