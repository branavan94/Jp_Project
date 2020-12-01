<template lang="html">
  <div>
    <b-row class="client-info my-3 mx-3 p-2 align-items-center" >
        <b-col md="2" v-for="info in infos" v-bind:key="info">
          <InfoComponent :group="info.type" :icon="info.icon"/>
        </b-col>
        <b-col class="state" md="2">
          <State :state="state"/>
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
      required:true
    },
    name: {
      type:String,
      required:true
    },
    phone: {
        type:String,
        required:true
      },
    group: {
        type:String,
        required:true
    },
    arrival: {
        type:String,
        required:true
    },
    departure: {
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
        },
        {
          type: this.phone,
          icon: ['fas', 'mobile-alt']
        },
        {
          type: this.arrival,
          icon: ['fas', 'plane-arrival']
        },
        {
          type: this.departure,
          icon: ['fas', 'plane-departure']
        }
      ]
    }
  }
};

</script>

<style lang="css" scoped>
.client-info{
  background-color:white;
  border: 1px solid #C9C9C9;
  border-radius : 15px;}
.state{
  border-left: 1px solid #FFD400;
}
</style>
