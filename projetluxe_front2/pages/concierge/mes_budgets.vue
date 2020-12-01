<template>
  <v-app>

    <div class="dashboard">
      <v-container class="my-5">
        <v-card class="mx-auto" v-for="project in projects" :key="project.client">
          <v-layout row wrap>
            <v-flex xs="12" md="6">
              <div class="caption grey--text">Nom du Client</div>
              <div>{{project.client}}</div>
            </v-flex>
            <v-flex xs="6" sm="4" md="2">
              <div class="caption grey--text">Accompagnant</div>
              <div>{{project.accompagnant}}</div>
            </v-flex>
            <v-flex xs="6" sm="4" md="2">
              <div class="caption grey--text">Numéro de téléphone</div>
              <div>{{project.telephone}}</div>
            </v-flex>
            <v-flex xs="2" sm="4" md="2">
              <div class="caption grey--text">Status</div>
              <div>{{project.status}}</div>
            </v-flex>
          </v-layout>
        </v-card>
      </v-container>
    </div>

  </v-app>
</template>

<script>


  export default {
    layout: 'nav',
    data() {
      return {
        projects: [
          { client: 'Pierre Marie', accompagnant: 'Jeanne Lou', telephone: '+3300000000', status: 'Modifications demandées' },
          { client: 'James Blon', accompagnant: 'Jeanne Lou', telephone: '+3300000000', status: 'En attente de validation' },
          { client: 'Thomas Dam', accompagnant: 'Jeanne Lou', telephone: '+3300000000', status: 'Planning Validé' }
        ]
      }

    }
}
</script>
