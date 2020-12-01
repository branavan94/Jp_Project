<template lang="html">
  <div>
    <b-row class="client-info my-3 mx-3 p-2 align-items-center" >
        <b-col md="2" v-for="info in infos" v-bind:key="info">
          <InfoComponent :group="info.type" :icon="info.icon"/>
        </b-col>
        <b-col md="2">
          <b-row class="cat justify-content-center pb-1"><p class="text-center mb-0"> Accordé </p></b-row>
          <b-row class="justify-content-center"><p class="text-center mb-0">{{accorde}}</p></b-row>
        </b-col>
        <b-col md="2">
          <b-row class="cat justify-content-center pb-1"><p class="text-center mb-0"> Estimé </p></b-row>
          <b-row class="justify-content-center"><p class="text-center mb-0">{{estime}}</p></b-row>
        </b-col>
        <b-col md="2">
          <b-row class="cat justify-content-center pb-1"><p class="text-center mb-0"> Consommé </p></b-row>
          <b-row class="justify-content-center"><p class="text-center mb-0">{{consomme}}</p></b-row>
        </b-col>
        <b-col class="state" md="2">
          <State :state="state" :billstate="billstate"/>
        </b-col>
   </b-row>
  </div>
</template>

<script>
import InfoComponent from '~/components/clientscomponents/InfoComponent.vue'
import State from '~/components/clientscomponents/State.vue'
export default {
  components: {
    State,
    InfoComponent
  },
  props:{
    state: {
      state:Boolean,
      required:false,
      billstate:Boolean,
      required:false
    },
    name: {
      type:String,
      required:true
    },
    group: {
      type:String,
      required:true
    },
    accorde: {
      type:String,
      required:true
    },
    consomme: {
      type:String,
      required:true
    },
    estime: {
      type:String,
      required:true
    }
  },
  data(){
    return{
      infos:[
        {
          type: this.name,
          icon: ['fas', 'user']
        },
        {
          type: this.group,
          icon: ['fas', 'users']
        }
      ]
    }
  }
}
</script>

<style lang="css" scoped>
.client-info{
  background-color:white;
  border: 1px solid #C9C9C9;
  border-radius : 15px;}
.state{
  border-left: 1px solid #FFD400;
}
.cat{
  color:#FFD400;
}
</style>
