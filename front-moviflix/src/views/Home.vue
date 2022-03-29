<template>
  <div class="ml-4">
    <h1>Page d'accueil</h1>
    <a class="nav-link" @click="logUserOut"> Logout</a>
    <p>Bienvenue {{user.name}}</p>
    
  </div>
</template>
<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
   data() {
    return {
      user: {}
    };
  },
  // methods: {
  //   getUserDetails() {
  //     let token = localStorage.getItem("jwt");
  //     let decoded = token; //find a way to decode
  //     this.user = decoded;
  //   },
  //   logUserOut() {
  //     localStorage.removeItem("jwt");
  //     this.$router.push("/");
  //   }
  // },
  // created() {
  //   this.getUserDetails();
  // }
})

export default class Home extends Vue {}
</script>
