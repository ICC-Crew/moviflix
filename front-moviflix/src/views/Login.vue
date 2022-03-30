<template>
  <div class="main-div">

    <div class="card">
      <div class="card-container">
        <div class="block text-center mb-5">
          <h1>Connectez-vous !</h1>
        </div>
        <form>
          <div class="block text-center border-round mb-5">
            <div class="p-input-icon-right p-float-label">
              <InputText id="username" class="p-inputtext-lg" type="text" v-model="loginData.username" />
              <label for="username">Pseudo</label>
              <i class="pi pi-user"/>
            </div>
          </div>
          <div class="block text-center border-round mb-3">
            <div class="p-input-icon-right p-float-label">
              <InputText id="password-input" class="p-inputtext-lg" type="password" v-model="loginData.password" />
              <label for="password-input">Password</label>
              <i class="pi pi-lock"/>
            </div>
          </div>
          <div class="block text-center border-round mb-5">
            <div class="div-text-reinitialize">
              <a>Mot de passe oublié ?</a>
            </div>
          </div>
          <div class="justify-center flex text-center border-round mb-5">
              <ButtonComp v-on:click="call_api_test()" id="login-submit-button" label="Connexion" icon="pi pi-sign-in"/>
              <ButtonComp v-on:click="goToRegister()" class="inscription-button" label="Inscription"/>
          </div>
        </form>
      </div>
    </div>

  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component';

@Options({
  data() {
    return {
      loginData: {
        username: "",
        password: ""
      }
    };
  },
  methods:{
    goToRegister : function(){
      this.$router.push('register'); 
    },
    call_api_test: async function (){
      fetch('http://localhost:3002/API/v1/users')
        .then(response => response.json())
        .then(console.log)}
    },
  computed: {}
})

export default class Login extends Vue {}
</script>
