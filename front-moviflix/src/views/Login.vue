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
              <ToastComp/>
              <ButtonComp v-on:click="api_login()" id="login-submit-button" label="Connexion" icon="pi pi-sign-in"/>
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
    addNewToken : function(token : string){
      this.$store.dispatch("addToken", token)
      this.$store.dispatch("connect")
    },
    goToRegister : function(){
      this.$router.push('register'); 
    },
    goToHome : function(){
      this.$router.push('/'); 
    },
    showSuccess() {
        this.$toast.add({severity:'success', summary: 'Succès', detail:'Connecté avec succès', life: 3000});
    },
    showError(message : string) {
        this.$toast.add({severity:'error', summary: 'Oups...', detail: message, life: 3000});
    },

    api_login: async function (){
      const requestOptions = {
        method: "POST",
        headers:{"Content-Type": "application/json"},
        body: JSON.stringify({userName: this.loginData.username, password: this.loginData.password})
      };
      await fetch('http://localhost:3002/API/v1/auth/user/login', requestOptions)
        .then((response) => response.json())
        .then((data) => {
          if('access_token' in data){
            this.addNewToken(data.access_token);
            this.showSuccess();
            setTimeout(this.goToHome,2000);
          }
          else{
            this.showError(data.detail);
          }
        });
      }
    },
  computed: {}
})

export default class Login extends Vue {}
</script>
