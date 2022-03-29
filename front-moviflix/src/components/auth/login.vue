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
              <InputText id="username" class="p-inputtext-lg" type="text" v-model="login.username" />
              <label for="username">Pseudo</label>
              <i class="pi pi-user"/>
            </div>
          </div>
          <div class="block text-center border-round mb-3">
            <div class="p-input-icon-right p-float-label">
              <InputText id="password-input" class="p-inputtext-lg" type="password" v-model="login.password" />
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
              <ButtonComp onclick="submit()" id="login-submit-button" type="submit" label="Connexion" icon="pi pi-sign-in"/>
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
      login: {
        email: "",
        password: ""
      }
    };
  },
  methods:{
    goToRegister : function(){
      this.$router.push('register'); 
    },
    async loginUser() {
      try {
        let response = await this.$http.post("/user/login", this.login);
        let token = response.data.token;
        localStorage.setItem("jwt", token);
        if (token) {
          console.log("Success", "Login Successful", "success");
          this.$router.push("/home");
        }
      } catch (err) {
        console.log("Error", "Something Went Wrong", "error");
        console.log(err.response);
      }
    }
  },
  computed: {}
})

export default class Login extends Vue {}
</script>
