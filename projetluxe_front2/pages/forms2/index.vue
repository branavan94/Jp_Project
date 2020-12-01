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
    <v-text-field v-model="id"
                  :counter="max"
                  :rules="rules"
                  label="Identifiant"></v-text-field>
    <v-text-field v-model="email"
                  :rules="emailRules"
                  label="E-mail"
                  required></v-text-field>


    <v-text-field v-model="match"
                  label="Mot de passe"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :rulesmdp="[rulesmdp.required, rulesmdp.min]"
                  :type="show1 ? 'text' : 'password'"
                  name="input-10-1"
                  
                  hint="At least 8 characters"
                  counter
                  @click:append="show1 = !show1"
          ></v-text-field>
    <v-text-field v-model="model"
                  :counter="max"
                  :rules="rules"
                  label="Confirmation Mot de Passe"></v-text-field>
    <v-checkbox v-model="checkbox"
                :rules="[v => !!v || 'You must agree to continue!']"
                label="confirmation check"
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
      allowSpaces: false,
      match: '',
      max: 0,
      model: '',
    }),
    data() {
      return {
        show1: false,
        rulesmdp: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          emailMatch: () => ('The email and password you entered don\'t match'),
        },
      }
    },
    computed: {
      rules() {
        const rules = []
        if (this.match) {
          const rule =
            v => (!!v && v) === this.match ||
              'Values do not match'

          rules.push(rule)
        }
        return rules
      },
    },
    watch: {
      match: 'validateField',
      max: 'validateField',
      model: 'validateField',
    },

    methods: {
      validate() {
        if (this.$refs.form.validate()) {
          this.snackbar = true
        }
      },
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
