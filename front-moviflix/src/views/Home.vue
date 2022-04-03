<template>
  <div class="ml-4">
    <h1>Page d'accueil</h1>
    <p>Bienvenue</p>
    
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
})

export default class Home extends Vue {}
</script>
