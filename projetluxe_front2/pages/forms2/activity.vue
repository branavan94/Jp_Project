<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Title"
      required
    ></v-text-field>
    


  <v-row justify="space-around">
    <v-date-picker v-model="picker"></v-date-picker>
    <v-time-picker v-model="e7" format="24hr"></v-time-picker>
  </v-row>


    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Address"
      required
    ></v-text-field>

    <v-text-field label="Budget"
                  
                  prefix="$"></v-text-field>
    


    <v-sheet class="pa-5">
    <v-switch v-model="switch1" inset :label="`Payé`"></v-switch>
    </v-sheet>

    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Contact"
      required
    ></v-text-field>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

     <v-container fluid>
    <v-radio-group v-model="column" column>
      <v-radio label="Hotel" value="Hotel"></v-radio>
      <v-radio label="Taxi" value="Taxi"></v-radio>
      <v-radio label="Réstaurant" value="Réstaurant"></v-radio>
      <v-radio label="Beauté" value="Beauté"></v-radio>
      <v-radio label="Visite" value="Visite"></v-radio>
      <v-radio label="Fashion Week" value="Fashion Week"></v-radio>
       <v-radio label="One to One" value="One to One"></v-radio>
       <v-radio label="Autre" value="Autre"></v-radio>
    </v-radio-group>
  </v-container>

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>

    

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate"
    >
      Validate
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Reset Form
    </v-btn>

    <v-btn
      color="warning"
      @click="resetValidation"
    >
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
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
      checkbox: false,
    }),

    data () {
      return {
        switch1: true,
      }
    },
     
    data () {
      return {
        e7: null,
      }
    },
     data () {
      return {
        picker: new Date().toISOString().substr(0, 10),
      }
    },

    
    

    methods: {
      validate () {
        if (this.$refs.form.validate()) {
          this.snackbar = true
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },
  }
</script>
