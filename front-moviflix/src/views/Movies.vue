<template>
  <Movie />
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Movie from '@/components/movies/Movie.vue'; // @ is an alias to /src

@Options({
  components: {
    Movie,
  },
})
export default class Movies extends Vue {}
</script>
