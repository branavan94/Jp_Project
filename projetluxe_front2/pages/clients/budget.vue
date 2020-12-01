<template lang="html">
  <div style='background-color:#F7F7F7'>
    <Header :logged="true" :loginpage="false"/>
    <div class="m-2 justify-content-center">
    <b-container class="d-flex justify-content-center pb-0 ">
      <b-badge class="headerclient align-middle w-50"><p class = "mb-0 my-2 w-100 py-auto align-middle">Mes budgets</p></b-badge>
    </b-container>

    <b-container class="align-middle py-0 shadow-sm">
      <b-row class="option-bar align-middle align-items-center">
        <b-col  sm="6" class=" align-middle">
          <b-form-select v-model="selected" :options="filters" size="sm" class="option-bar w-50">
          </b-form-select>
        </b-col>


        <b-col sm=6 class="">
            <b-form inline class="justify-content-sm-end pr-2 justify-content-start">
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
      <Budget v-for="budget in budgets" v-bind:key="budget"
        :name="budget.name"
        :group="budget.group"
        :accorde="allocated"
        :estime="estimated"
        :consomme="used"
        :state="stateBT"/>
    </b-container>
    </div>
  </div>


</template>

<script>
import Header from '~/components/Header.vue'
import Budget from '~/components/clientscomponents/Budget.vue'
export default {
  components: {
    Header,
    Budget
  },
  async asyncData ({ $axios, params }) {
    try{
      var budgets = [];
      let clients = await $axios.$get(`/Client/`)
      clients.forEach((client) => {
        var budget = {
          name : client.name + " " +client.last_name,
          group : client.zone,
          planning : client.plan,
          accorde: 0,
          estime: 0,
          consomme:0
        }
        budgets.push(budget);
      });
      console.log(budgets);
      return {budgets}
    }
    catch(e){
      return { budgets: [] };
    }
  },
  data(){
    return{
      budgets:[],
      allocated: "50 000",
      estimated:"47 000",
      used: "22 000",
      stateT: true,
      stateF: false,
      stateBT:true,
      stateBF:false,
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
