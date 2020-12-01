import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'// Ensure you are using css-loader version "^2.1.1" ,
Vue.use(Vuetify)

export default ctx => {
  const vuetify = new Vuetify({
    theme: {
      themes: {
        light: {
          primary: '#FFD400',
          secondary: '#514D4D',
          accent: '#8c9eff',
          error: '#b71c1c',
        },
      },
    },
    icons: {
      iconfont: 'md',
    },
  })

  ctx.app.vuetify = vuetify
  ctx.$vuetify = vuetify.framework
}
