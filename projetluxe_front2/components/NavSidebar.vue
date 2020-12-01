<template>
  <nav>
    <v-app-bar app dense  extension-height="35px">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>
        <v-col align="center" justify="center">
          
          <div class="title">FW Manager</div>
        </v-col>
      </v-toolbar-title>
      <!-- <v-col align="center" justify="center">
    <v-img class="image" :src="require('~/assets/logoJP.png')" width="80" height="47"></v-img>
    <div class="title">FW Manager</div>
        
  </v-col>-->

      <v-spacer></v-spacer>


      <v-toolbar-items class="toolbar1">
        <v-btn text>LANGUE</v-btn>

        <v-btn @click="logout" text>DECONNEXION</v-btn>
        <v-btn icon>
          <v-icon>info</v-icon>
        </v-btn>
      </v-toolbar-items>
      <template v-slot:extension>

        <v-toolbar-items>

          <v-btn text to="/market">ACCUEIL</v-btn>
          <v-btn text to="/clients">MES CLIENTS</v-btn>
          <v-btn text to="/inbox">MA MESSAGERIE</v-btn>
        </v-toolbar-items>
        <v-spacer></v-spacer>
      </template>
    </v-app-bar>
    <v-navigation-drawer app v-model="drawer" class="secondary">
      <v-layout column align-center>
        <v-flex class="mt-6">
          
            <v-img class="image" :src="require('~/assets/logoJP.png')" width="80" height="47"></v-img>
          
        </v-flex>
      </v-layout>
      <v-list>
        <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
          <v-list-item-action>
            <v-icon class="white--text">{{link.icon}}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="white--text">{{link.text}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list>
          <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
            <v-list-item-action>
              <v-icon class="white--text">{{link.icon}}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="white--text">{{link.text}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>


<script>
  export default {
    data() {
      return {
        drawer: false,
        links: [
          { icon: 'assignment_ind', text: 'Mes Clients', route: '/clients' },
          { icon: 'mail', text: 'Ma Messagerie', route: '/inbox' },
          { icon: 'attach_money', text: 'Mes Budgets', route: '/clients/budget' },
        ]

      }
    },
  methods: {
    logout(){
      this.$store.commit('userStore/setUserLogged', {});
      window.location.href="/"

    }
  }
  }
</script>
<style scoped>

  .title {
    color: #FFD400;
    font-size: 20px;
    text-align: center;
  }
  .toolbartitle{

  }
  .image {
    position: center;
  }

</style>





<!--<template>
  <div>
    <b-button v-b-toggle.collapse-1 variant="primary" data-toggle="collapse" data-target="#demo">Toggle Collapse</b-button>
    <b-collapse id="collapse-1" class="mt-2">
      <b-card >
        <p class="card-text" >Collapse contents Here</p>
        <b-button v-b-toggle.collapse-1-inner size="sm">Toggle Inner Collapse</b-button>
        <b-collapse id="collapse-1-inner" class="mt-2">
          <b-card>Hello!</b-card>
        </b-collapse>
      </b-card>
      <b-card>
        <p class="card-text">Collapse contents Here</p>
        <b-button v-b-toggle.collapse-2-inner size="sm">Toggle Inner Collapse</b-button>
        <b-collapse id="collapse-2-inner" class="mt-2">
          <b-card>Hello!</b-card>
        </b-collapse>
      </b-card>
    </b-collapse>
  </div>
  </template>
<style scoped>
  .collapse {
    visibility: hidden;

  }

    .collapse.show {
      visibility: visible;
      display: block;

    }

  .collapsing {
    position: relative;
    height: 0;
    overflow: hidden;
    -webkit-transition-property: height, visibility;
    transition-property: height, visibility;
    -webkit-transition-duration: 0.35s;
    transition-duration: 0.35s;
    -webkit-transition-timing-function: ease;
    transition-timing-function: ease;

  }

    .collapsing.width {
      -webkit-transition-property: width, visibility;
      transition-property: width, visibility;
      width: 0;
      height: auto;

    }


</style>-->
<!--<template>

  <div class="wrapper">

    <nav id="sidebar">
      <div class="sidebar-header">
        <h3>Bootstrap Sidebar</h3>
      </div>

      <ul class="list-unstyled components">
        <p>Dummy Heading</p>
        <li class="active">
          <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Home</a>
          <ul class="collapse list-unstyled" id="homeSubmenu">
            <li>
              <a href="#">Home 1</a>
            </li>
            <li>
              <a href="#">Home 2</a>
            </li>
            <li>
              <a href="#">Home 3</a>
            </li>
          </ul>
        </li>
        <li>
          <a href="#">About</a>
        </li>
        <li>
          <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Pages</a>
          <ul class="collapse list-unstyled" id="pageSubmenu">
            <li>
              <a href="#">Page 1</a>
            </li>
            <li>
              <a href="#">Page 2</a>
            </li>
            <li>
              <a href="#">Page 3</a>
            </li>
          </ul>
        </li>
        <li>
          <a href="#">Portfolio</a>
        </li>
        <li>
          <a href="#">Contact</a>
        </li>
      </ul>
    </nav>

  </div>
</template>
<style scoped>
  body {
    font-family:  sans-serif;
    background: #fafafa;
  }

  p {
    font-family: sans-serif;
    font-size: 1.1em;
    font-weight: 300;
    line-height: 1.7em;
    color: #999;
  }

  a, a:hover, a:focus {
    color: inherit;
    text-decoration: none;
    transition: all 0.3s;
  }
  .wrapper {
    display: flex;
    align-items: stretch;
  }
  a[data-toggle="collapse"] {
    position: relative;
  }

  .dropdown-toggle::after {
    display: block;
    position: absolute;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
  }

    #sidebar.active {
      margin-left: -250px;
    }
  #sidebar {
    /* don't forget to add all the previously mentioned styles here too */
    min-width: 250px;
    max-width: 250px;
    background: #7386D5;
    color: #fff;
    transition: all 0.3s;
  }

    #sidebar .sidebar-header {
      padding: 20px;
      background: #6d7fcc;
    }

    #sidebar ul.components {
      padding: 20px 0;
      border-bottom: 1px solid #47748b;
    }

    #sidebar ul p {
      color: #fff;
      padding: 10px;
    }

    #sidebar ul li a {
      padding: 10px;
      font-size: 1.1em;
      display: block;
    }

      #sidebar ul li a:hover {
        color: #7386D5;
        background: #fff;
      }

    #sidebar ul li.active > a, a[aria-expanded="true"] {
      color: #fff;
      background: #6d7fcc;
    }

  ul ul a {
    font-size: 0.9em !important;
    padding-left: 30px !important;
    background: #6d7fcc;
  }
  @media (max-width: 768px) {
    #sidebar {
      margin-left: -250px;
    }

      #sidebar.active {
        margin-left: 0;
      }
  }
</style> -->
