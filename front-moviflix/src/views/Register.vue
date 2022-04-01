<template>
  <div class="main-div">

    <div class="card">
      <div class="card-container">
        <div class="block text-center mb-5">
          <h1>Créez un compte !</h1>
        </div>
        <form>
         <div class="block text-center border-round mb-5">
            <div class="p-input-icon-right p-float-label">
              <InputText id="email" class="p-inputtext-lg" type="text" v-model="registerData.email" />
              <label for="email">Email</label>
              <i class="pi pi-envelope"/>
            </div>
          </div>
          <div class="block text-center border-round mb-5">
            <div class="p-input-icon-right p-float-label">
              <InputText id="username" class="p-inputtext-lg" type="text" v-model="registerData.username" />
              <label for="username">Pseudo</label>
              <i class="pi pi-user"/>
            </div>
          </div>
          <div class="block text-center border-round mb-5">
            <div class="p-input-icon-right p-float-label">
              <Password id="password" class="p-inputtext-lg" v-model="registerData.password">
                <template #header>
                    <h6>Choississez un mot de passe</h6>
                </template>
                <template #footer>
                    <Divider />
                    <p class="mt-2">Suggestions</p>
                    <ul class="pl-2 ml-2 mt-0" style="line-height: 1.5">
                        <li>Au moins une minuscule</li>
                        <li>Au moins une majuscule</li>
                        <li>Au moins un caractère numérique</li>
                        <li>Minimum 8 caractères</li>
                    </ul>
                </template>
              </Password>
              <label for="password">Mot de passe</label>
              <i class="pi pi-lock"/>
            </div>
          </div>
          <div class="block text-center border-round mb-5">
            <ToastComp/>
            <ButtonComp v-on:click="api_register()" id="register-submit-button" type="button" label="Submit" icon="pi pi-sign-in"/>
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
      registerData: {
        username: "",
        password: "",
        email: ""
      }
    };
  },
  methods:{
    goToHome : function(){
      this.$router.push('/'); 
    },
    showSuccess() {
        this.$toast.add({severity:'success', summary: 'Succès', detail:'Inscription réussie !', life: 3000});
    },
    showError(message : string) {
      this.$toast.add({severity:'error', summary: 'Oups...', detail: message, life: 3000});
    },
    api_register: async function (){
      const requestOptions = {
        method: "POST",
        headers:{"Content-Type": "application/json"},
        body: JSON.stringify({userName: this.registerData.username, password: this.registerData.password, email: this.registerData.email})
      };
      await fetch('http://localhost:3002/API/v1/users', requestOptions)
        .then((response) => response.json())
        .then((data) => {
          console.log("data",data);
          if(data == undefined){
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

export default class Register extends Vue {}
</script>