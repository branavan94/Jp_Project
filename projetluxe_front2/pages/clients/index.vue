<template lang="html">
  <div style='background-color:#F7F7F7'>
    <Header :logged="true" :loginpage="false"/>
    <div class="m-2">
    <b-container class="d-flex justify-content-center pb-0 ">
      <b-badge class="headerclient align-middle w-50"><p class = "mb-0 my-2 w-100 py-auto align-middle">Mes clients</p></b-badge>
    </b-container>

    <b-container class="align-middle py-0 shadow-sm">
      <b-row class="option-bar align-middle align-items-center">
        <b-col  sm="6" class=" align-middle">
          <b-form-select v-model="selected" :options="filters" size="sm" class="option-bar w-50">
          </b-form-select>
        </b-col>


        <b-col sm=6 class="">
          <b-form inline class="justify-content-md-end px-2 justify-content-start">

            <b-button size="sm" class="search-button" type="submit" >
              <font-awesome-icon :icon="['fas', 'search']" class="align-middle m-2"/>
            </b-button>
            <b-form-input class="search-bar" placeholder="Rechercher...">
              <b-input size="sm" class="l  pl-1" ></b-input>
            </b-form-input>

          </b-form>
        </b-col>

      </b-row>
    </b-container>

    <b-container class="bv-example-row py-0">
      <Client v-for="client in clients" v-bind:key="client"
      :name="client.last_name" :group="client.zone" :phone="client.telephone" :arrival="client.date_arrival" :departure="client.date_leave" :state="stateT"/>
    </b-container>
    </div>
  </div>


</template>

<script>
import Header from '~/components/Header.vue'
import Client from '~/components/clientscomponents/Client.vue'
export default {
  components: {
    Header,
    Client
  },
  async asyncData({ $axios, params }) {
    try {
      let clients = await $axios.$get(`/Client/`);
      clients.forEach((element)=>{
        element.last_name = element.name + " " + element.last_name;
        element.date_leave = element.date_leave.substring(0,10) + " " + element.date_leave.substring(11,19);
        element.date_arrival = element.date_arrival.substring(0,10) + " " + element.date_arrival.substring(11,19)
      })
      return { clients };
    } catch (e) {
      return { clients: [] };
    }
  },
  data(){
    return{
      clients:[],
      stateT: true,
      stateF: false,
      selected: null,
      filters:[
        { value: null, text: 'Filtre' },
        { value: 'A', text: 'Modifications' },
        { value: 'B', text: 'Départs' }
      ]
    }
  }

}
</script>

<style lang="css" scoped>
.option-bar{
  background-color: #FFD400;
  border-color: #FFD400;
  color: white;
}
.headerClient{
  border-top: solid 1px;
  border-right: solid 1px;
  border-left: solid 1px;
  border-radius: 25px;
  background-color: white;
}
.headerclient{
  border-radius : 10px 10px 0px 0px;
  background-color: white;
  color: #FFD400;
}
.search-bar{
  border-radius: 0px;
  border-color: white;
  background-color:white;
}
.search-button{
  border-radius: 0px;
  color: #FFD400;
  background-color:white;
  border-color: white;
}
.search{
  background-color:white;
}
</style>
