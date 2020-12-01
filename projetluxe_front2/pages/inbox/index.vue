<template lang="html">
  <section>
    <div class="back">
      <b-row class="inbox h-100 overflow-hidden">
        <b-col cols="2" class="justify-content-center m-3">

          <b-row class="justify-content-center mb-5">
            <b-button pill class="button btn-block align-self-center" @click="newDraft()" >
              <font-awesome-icon :icon="['fas', 'plus']" class="align-self-center"/><p class="d-none d-sm-inline  align-self-center ml-2 mb-0 my-1 mx-4 small">NOUVEAU MESSAGE</p>
            </b-button>
          </b-row>

          <b-row class="align-items-left">
            <b-button class="categories p-1" to="/inbox">
              <font-awesome-icon :icon="['fas', 'envelope']" class="mail-icons align-self-center"/>
              <p class="d-none d-sm-inline ml-3">Reçus</p>
            </b-button>
          </b-row>

          <b-row class="align-items-left ">
            <b-button class="categories p-1" to="/inbox/sent">
              <font-awesome-icon :icon="['fas', 'envelope-open-text']" class="mail-icons align-self-center "/>
              <p class="d-none d-sm-inline ml-3">Envoyés</p>
            </b-button>
          </b-row>

          <b-row class="align-items-left ">
            <b-button class="categories p-1" to="/inbox/drafts">
              <font-awesome-icon :icon="['fas', 'paperclip']" class="mail-icons align-self-center "/>
              <p class="d-none d-sm-inline ml-3">Brouillons</p>
            </b-button>
          </b-row>
        </b-col>

        <b-col  class="mails py-0 overflow-auto">
          <NuxtChild :key="$route.params"/>
        </b-col>
      </b-row>
    </div>
  </section>
</template>

<script type="text/javascript">
export default{
  methods:{
    newDraft(){
      this.$store.commit('mailStore/setDraftM', null);
      this.$router.push('/inbox/new');
    }
  }
}
</script>

<style lang="css" scoped>
.back{
  background-color:#F7F7F7;
}
.button {
  font: inherit;
  background-color: #FFD400;
  color: white;
  padding: 5px;
  cursor: pointer;
  border: 1px solid #FFD400;
  border-radius: 3px;
}
.button:hover,
.button:active:focus {
  background-color: #FFD400;
  border: 1px solid #FFD400;
}
.inverted {
  background-color: #FFD400;
  color: black;
  border: 1px solid transparent;
}
.inverted:hover,
.inverted:active:focus {
  color: #FFD400;
  background-color: #FFD400;
  border: 1px solid transparent;
}

.inbox{
  background-color: white;
  max-height: 75vh;
  border: 1px solid #C9C9C9;
  border-radius: 5px;
}
.mails{
  border-left: 1px solid #C9C9C9;
  max-height:75vh;
}
.categories{
  color: #C9C9C9;
  background-color:white;
  border-color:white;
}
.mail-icons{
  color: #FFD400;
}
</style>
