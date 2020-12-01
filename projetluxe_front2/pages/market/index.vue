<template>
  <v-app>
    <div class="team">
      <v-container class="my-5">
        <v-layout row wrap>
          <v-flex xs12 sm6 md4 lg3 v-for="market in  markets" :key="market.continent">
            <v-card class="text-xs-center ma-3">
              <v-img class="white--text align-end"
                     height="200px"
                     :src="market.image">
                <v-card-title>{{market.name}}</v-card-title>
              </v-img>
              <v-card-text>
                <div class="title">{{market.continent}}</div>
                <div class="body-2">{{market.evenement}}</div>
                <div class="grey--text">{{market.dates}}</div>
              </v-card-text>
              <v-card-actions>
                <v-btn text to="/superviseur">
                  <v-icon small left color="grey">bookmark</v-icon>
                  <span class="grey--text">Accés</span>
                </v-btn>
                <v-btn text to="/forms2/client">
                  <v-icon small left color="grey">people</v-icon>
                  <span class="grey--text">Ajouter VIP</span>
                </v-btn>
              </v-card-actions>
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
    data() {
      return {
        markets: [
          { name: 'Dior', continent: 'Asie', evenement: 'Fashion Week 2020 Femme', dates: '01/09/2020 - 07/09/2020', image: 'https://weekend.lesechos.fr/medias/2020/01/21/2320494_fashion-week-haute-couture-printemps-ete-2020-les-deesses-de-dior-web-tete-0602617932634.jpg' },
          { name: 'Dior', continent: 'Afrique', evenement: 'Fashion Week 2020 Femme', dates: '01/09/2020 - 07/09/2020', image: 'https://yard.media/wp-content/uploads/2017/07/SLIDE_001.jpg' },
          { name: 'Dior', continent: 'Amérique du Nord', evenement: 'Fashion Week 2020 Femme', dates: '01/09/2020 - 07/09/2020', image: 'https://www.letelegramme.fr/ar/imgproxy.php/images/2018/09/24/fashion-week-dior-ouvre-le-bal_4182132_1000x526.jpg?article=20180924-1012088300&aaaammjj=20180924' },
          { name: 'Dior', continent: 'Amérique du Sud', evenement: 'Fashion Week 2020 Femme', dates: '01/09/2020 - 07/09/2020', image: 'https://www.vanityfair.fr/uploads/images/thumbs/202004/a6/vf_dior_hc_pe20_slider_9757.jpeg_north_375x310_.jpg' }
        ]
      }
    }
  }
</script>
