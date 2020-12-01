<template>
  <v-form ref="form"
          v-model="valid"
          lazy-validation>
    <v-text-field v-model="name"
                  :counter="10"
                  :rules="nameRules"
                  label="Prénom"
                  required></v-text-field>

    <v-text-field v-model="lastname"
                  :counter="10"
                  :rules="nameRules"
                  label="Nom"
                  required></v-text-field>
    <v-select v-model="select"
              :items="items"
              :rules="[v => !!v || 'Marché is required']"
              label="Marché"
              required></v-select>

    <v-select v-model="select2"
              :items="items2"
              :rules="[v => !!v || 'Langue is required']"
              label="Langue"
              required></v-select>

    <v-text-field v-model="value"
                  v-mask="mask"
                  label="Contact"></v-text-field>

    <v-checkbox v-model="disabled" class="mx-2" label="Accompagné"></v-checkbox>

    <v-text-field v-model="nameacc"
                  :counter="10"
                  :disabled="!disabled"
                  label="Prénom  accompagnateur"
                  required></v-text-field>

    <v-text-field v-model="lastnameacc"
                  :counter="10"
                  :disabled="!disabled"
                  label="Nom accompagnateur"
                  required></v-text-field>
    <v-row>
      <v-col cols="6" sm="6" md="4">
        <v-menu ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                :return-value.sync="date"
                transition="scale-transition"
                offset-y
                min-width="290px">
          <template v-slot:activator="{ on }">
            <v-text-field v-model="date"
                          label="Date d'arrivée"
                          prepend-icon="event"
                          readonly
                          v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="date" no-title scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
            <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
          </v-date-picker>
        </v-menu>
      </v-col>
      <v-col cols="6" sm="6" md="4">
        <v-menu ref="menu2"
                v-model="menu2"
                :close-on-content-click="false"
                :return-value.sync="date2"
                transition="scale-transition"
                offset-y
                min-width="290px">
          <template v-slot:activator="{ on }">
            <v-text-field v-model="date2"
                          label="Date de départ"
                          prepend-icon="event"
                          readonly
                          v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="date2" no-title scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="menu2 = false">Cancel</v-btn>
            <v-btn text color="primary" @click="$refs.menu2.save(date2)">OK</v-btn>
          </v-date-picker>
        </v-menu>
      </v-col>
    </v-row>
    <v-text-field label="Budget"
                  
                  prefix="$"></v-text-field>
    <v-checkbox v-model="checkbox"
                :rules="[v => !!v || 'You must agree to continue!']"
                label="check"
                required></v-checkbox>

    <v-btn :disabled="!valid"
           color="success"
           class="mr-4"
           @click="validate">
      Validate
    </v-btn>

    <v-btn color="error"
           class="mr-4"
           @click="reset">
      Reset Form
    </v-btn>

    <v-btn color="warning"
           @click="resetValidation">
      Reset Validation
    </v-btn>
  </v-form>
</template>
<script>
  
  export default {

    layout: 'nav',

    data: () => ({
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
    
      select: null,
      select2: null,
      items2: [
        'Chinois',
        'Français',
        'Anglais',
        'Italien',
      ],
      checkbox: false,
      allowSpaces: false,
      match: '',
      max: 0,
      model: '',
      items: [
        'Asie',
        'Afrique',
        'Amérique du Nord',
        'Europe',
      ],
      disabled: false,
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      menu2: false,
      date2: new Date().toISOString().substr(0, 10)

    }),


    methods: {

      reset() {
        this.$refs.form.reset()
      },
      resetValidation() {
        this.$refs.form.resetValidation()
      },
      validateField() {
        this.$refs.form.validate()
      },
    },

  }
</script>
