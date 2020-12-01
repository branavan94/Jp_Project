<template>
  <v-app>
    <div class="dashboard">
      <v-container class="my-5">
        <v-layout row wrap class="layouttabdebord" justify>
          <v-flex xs12 md12>
            <v-card class="mx-auto primary">
              <v-card-text>
                <div class="tabdebord">Tableau de Bord</div>
                <v-layout row wrap justify>
                  <v-flex xs12 md3>
                    <div class="undertabdebord caption white--text">User</div>
                  </v-flex>
                  <v-flex xs4 sm4 md3>
                    <div class="undertabdebord caption white--text">Maison de Mode</div>
                  </v-flex>
                  <v-flex xs4 sm4 md3>
                    <div class="undertabdebord caption white--text">Dates du projet</div>
                  </v-flex>
                  <v-flex xs4 sm4 md3>
                    <div class="undertabdebord caption white--text">Marché</div>
                  </v-flex>
                </v-layout>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
        <!--under "tableau de bord"-->
        <v-layout class="layoutdash" row wrap justify-center>
          <v-flex xs12 md8 class="clientflex">
            <!--card with key numbers-->
            <v-card color="white" class=" mx-auto" flat>
              <v-card-text>
                <v-layout row wrap justify-center>
                  <v-flex xs2 sm2 md2>
                    <div class="chiffrescle  ">03</div>
                  </v-flex>
                  <v-flex xs2 sm2 md2>
                    <div class="chiffrescle  ">08</div>
                  </v-flex>
                  <v-flex xs2 sm2 md2>
                    <div class="chiffrescle  ">10</div>
                  </v-flex>
                </v-layout>
                <v-layout row wrap justify-center>
                  <v-flex xs2 sm2 md2>
                    <div class="undertabdebord caption ">Guests</div>
                  </v-flex>
                  <v-flex xs2 sm2 md2>
                    <div class="undertabdebord caption ">Planning à valider</div>
                  </v-flex>
                  <v-flex xs2 sm2 md2>
                    <div class="undertabdebord caption ">Messages</div>
                  </v-flex>

                </v-layout>
                <div class="layoutchiffrecle"></div>
              </v-card-text>

            </v-card>
            <div class="backgroundlistclient">
              <div class="tabdebudget pa-2">MES CLIENTS</div>
              <!--card with client list-->
              <v-card :class="` project ${project.status}`" flat v-for="project in projects" :key="project.client">
                <v-layout row wrap class="layoutlistclients" justify-center>
                  <v-flex xs12 md3>
                    <div class="caption grey--text">Nom du Client</div>
                    <div class="infoclient">{{project.client}}</div>
                  </v-flex>
                  <v-flex xs4 sm4 md3>
                    <div class="caption grey--text">Accompagnant</div>
                    <div class="infoclient">{{project.accompagnant}}</div>
                  </v-flex>
                  <v-flex xs4 sm4 md3>
                    <div class="caption grey--text">Numéro de téléphone</div>
                    <div class="infoclient">{{project.telephone}}</div>
                  </v-flex>
                  <v-flex xs4 sm4 md3>
                    <div class="caption grey--text">Status</div>
                    <div v-if="project.status=='validate'"><v-chip :class="`${project.status} white--text caption my-2`">Planning validé</v-chip></div>
                    <div v-if="project.status=='modification'"><v-chip :class="`${project.status} white--text caption my-2`">Modification demandée</v-chip></div>
                    <div v-if="project.status=='waiting'"><v-chip :class="`${project.status} white--text caption my-2`">En attente de validation</v-chip></div>
                  </v-flex>
                </v-layout>
                <v-divider></v-divider>
              </v-card>
            </div>
            <v-btn text to="/forms2">
              <v-icon small left color="grey">people</v-icon>
              <span class="grey--text">Ajouter un client</span>
            </v-btn>
            <!--flex of budget class-->
          </v-flex>
          <v-flex xs12 md3 class="budget">
            <!--general budget-->
            <v-card class="mx-auto" color="transparent" flat>
              <v-card-text>
                <div class="tabdebudget pa-1">MES BUDGETS</div>
                <div class="tabdebudget pa-0">Total accordé:------------------199000</div>
                <div class="tabdebudget pa-0">Total estimé:-------------------199000</div>
                <div class="tabdebudget pa-0">Total consommé:--------------199000</div>
              </v-card-text>

            </v-card>
            <v-card class="mx-auto" color="transparent" flat>
              <v-card-text>
                <div class="tabdebudget pa-0"> BUDGET PAR CLIENT</div>
              </v-card-text>

            </v-card>
            <!--list of budget-->
            <v-card class="mx-auto" flat v-for="budget in budgets" :key="budget.key">
              <v-layout row wrap class="layoutlistclients" justify-center>
                <v-flex xs12 sm12 md12>

                  <div class=" budgetlistclient">{{budget.client}}</div>
                </v-flex>
                <v-flex xs4 sm4 md4>
                  <div class=" budgetlist caption grey--text">Accordé</div>
                  <div class=" budgetlistchiffre">{{budget.accorde}}</div>
                </v-flex>
                <v-flex xs4 sm4 md4>
                  <div class="budgetlist caption grey--text">Estimé</div>
                  <div class=" budgetlistchiffre">{{budget.estime}}</div>
                </v-flex>
                <v-flex xs4 sm4 md4>
                  <div class="budgetlist caption grey--text">Consommé</div>
                  <div class="budgetlistchiffre">{{budget.consomme}}</div>
                </v-flex>

              </v-layout>
              <v-divider></v-divider>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </div>

  </v-app>

</template>

<script>
  import Header from '~/components/Header.vue'

  export default {
    components: {
      Header,

    },
    middleware: ['fakeMails'],
    layout: 'nav',

    computed: {
      user() {
        return this.$store.state.userStore.userLogged
      }

    },
    async asyncData({ $axios, params }) {
      try {
        let clients = await $axios.$get(`/Client/`);
        clients.forEach((element)=>{
          element.last_name = element.name + " " + element.last_name;
          element.date_leave = element.date_leave.substring(0,10) + " " + element.date_leave.substring(11,19);
          element.date_arrival = element.date_arrival.substring(0,10) + " " + element.date_arrival.substring(11,19)
          if(!element.accompanied)
          {
            element.accompagnied = "N/A";
          }
        })
        return { clients };
      } catch (e) {
        return { clients: [] };
      }
    },
    data() {
      return {
        clients:[],
        projects: [
          { client: 'Pierre Marie', accompagnant: 'Jeanne Lou', telephone: '+3300000000', status: 'modification' },
          { client: 'James Blon', accompagnant: 'Jeanne Lou', telephone: '+3300000000', status: 'waiting' },
          { client: 'Thomas Dam', accompagnant: 'Jeanne Lou', telephone: '+3300000000', status: 'validate' }
        ],
        budgets: [
          { key: '1', accorde: '73000', estime: '70000', consomme: '33000', client: 'Thomas Dam'},
          { key: '1', accorde: '73000', estime: '70000', consomme: '33000', client: 'James Blon'},
          { key: '1', accorde: '73000', estime: '70000', consomme: '33000', client: 'Pierre Marie'}
        ]
      }
    }
  }
</script>

<style>
  .project.validate {
    border-left: 4px solid #00980A;
  }

  .project.modification {
    border-left: 4px solid #CD1B1B;
  }

  .project.waiting {
    border-left: 4px solid #EAA607;
  }

  .v-chip.waiting {
    background: #EAA607;
  }

  .v-chip.validate {
    background: #00980A;
  }

  .v-chip.modification {
    background: #CD1B1B;
  }

  .tabdebord {
    margin: 0 auto;
    padding-bottom: 15px;
    padding-top: 5px;
    width: 200px;
    text-align: center;
    color: white;
    font-size: 20px;
  }

  .tabdebudget {
    margin: 0 auto;
    padding-bottom: 15px;
    padding-top: 5px;
    width: 200px;
    text-align: center;
    font-size: 12px;
    color: #707070;
    font-weight: bold;
  }

  .undertabdebord {
    margin: 0 auto;
    text-align: center;
    color: #707070;
    font-size: 20px;
  }

  .chiffrescle {
    margin: 0 auto;
    text-align: center;
    color: #707070;
    font-size: 25px;
  }

  .layoutlistclients {
    padding-left: 20px;
    padding-right: 20px;
    padding-bottom: 0px;
    padding-top: 15px;
  }

  .layoutchiffrecle {
    margin-top: 10px;
    margin-left: 20%;
    margin-right: 20%;
    border-bottom: 1.5px solid #FFD400;
  }

  .layouttabdebord {
    padding-left: 0px;
    padding-right: 0px;
    padding-bottom: 10px;
    padding-top: 0px;
  }

  .infoclient {
    font-size: 15px;
  }

  .budgetlist {
    text-align: center;
  }

  .budgetlistchiffre {
    text-align: center;
    font-size: 12px;
  }

  .budgetlistclient {
    padding-bottom: 5px;
    text-align: center;
    font-size: 12px;
  }

  .budget {
    padding-left: 10px;
    padding-right: 10px;
    margin-top: 20px;
    margin-bottom: 20px;
    margin-right: 0px;
    background-color: #E3E3E3;
  }

  .clientflex {
    padding-left: 10px;
    padding-right: 10px;
  }

  .layoutdash {
    background-color: white;
  }

  .backgroundlistclient {
    padding: 5px;
    background-color: #E3E3E3;
  }
</style>
