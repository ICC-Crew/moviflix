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
              <InputText id="email" class="p-inputtext-lg" type="text" v-model="register.email" />
              <label for="email">Email</label>
              <i class="pi pi-envelope"/>
            </div>
          </div>
          <div class="block text-center border-round mb-5">
            <div class="p-input-icon-right p-float-label">
              <InputText id="username" class="p-inputtext-lg" type="text" v-model="register.name" />
              <label for="username">Pseudo</label>
              <i class="pi pi-user"/>
            </div>
          </div>
          <div class="block text-center border-round mb-5">
            <div class="p-input-icon-right p-float-label">
              <Password id="password" class="p-inputtext-lg" v-model="register.password">
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
            <ButtonComp id="register-submit-button" type="submit" label="Submit" icon="pi pi-sign-in"/>
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
        name: "",
        password: ""
      }
    };
  },
  methods:{
    async registerUser() {
      try {
        let response = await this.$http.post("/user/register", this.register);
        console.log(response);
        let token = response.data.token;
        if (token) {
          localStorage.setItem("jwt", token);
          this.$router.push("/");
          console.log("Success", "Registration Was successful", "success");
        } else {
          console.log("Error", "Something Went Wrong", "error");
        }
      } catch (err) {
        let error = err.response;
        if (error.status == 409) {
          console.log("Error", error.data.message, "error");
        } else {
          console.log("Error", error.data.err.message, "error");
        }
      }
    }
  },
  computed: {}
})

export default class Register extends Vue {}
</script>
