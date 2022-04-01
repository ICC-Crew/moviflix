<template>
  <h1>
  Film
  </h1>
   <div v-if="loading">
            <ProgressBar mode="indeterminate" />
    </div>

    <div v-if="error">{{ error }}</div>

    <div v-if="movie">
        <div class ="flex justify-content-evenly flex-wrap">
        <div>
            <CardComp class="m-4" style="width : 35rem">
                <template #header>
                    <img :src="movie.movieCoverUrl" loading="lazy" >
                </template>
                <template #title>
                    {{ movie.title }}
                </template>
                <template #content>
                 {{ movie.synopsis }}
                </template>
            </CardComp>
            </div>
            <div v-if="movie.trailerUrl">
          <iframe :src="processUrlTrailer" width="640" height="640" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" frameborder="no" scrolling="no"></iframe>
            <DividerComp />
            <div> Réalisateurs 
            <h2 v-for="director in movie.directors" :key="director[i]">
            {{ director }}
            </h2>
            <DividerComp />
            Durée
            <h2>
            {{ movie.duration }} min
            </h2>
            <DividerComp />
            Sortie
            <h2>
            {{ movie.year }}
            </h2>
            <DividerComp />
            <ChipComp v-for="genre in movie.genres" :key="genre[i]" :label="genre" class="m-2" style="background: var(--primary-color);color: var(--primary-color-text)" />
            </div>
            </div>
      </div>
      <div class ="flex justify-content-evenly flex-wrap">
            <CardComp v-for="actor in movie.actors" :key="actor[i]" class="m-2" style="width : 10rem">
                <template #header>
                    <img :src="actor.imgActorUrl" loading="lazy" >
                </template>
                <template #title>
                    {{ actor.name }}
                </template>
                <template #content>
                 {{ actor.asCharacter }}
                </template>
            </CardComp>     
      </div>

    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  data() {
    return {
      loading: false,
      movie: null,
      error: null,

    }
  },
  created() {
    this.fetchMovie(this.$route.params.id)
  },
  methods: {
    fetchMovie : async function(movieId:string){
      this.loading = true
      this.error = this.movie = null
      fetch(`http://localhost:3002/API/v1/movies/${movieId}`)
        .then(response => {
            if (response.ok){
                return response.json() 
            }      
            throw new Error('Erreur lors de la connection à l API')
        })
        .then(responseJSON =>{
            this.movie = responseJSON
            this.loading = false
        })
        .catch((error)=>{
            this.error = error.toString()
            this.loading = false
            console.log(error)
        })
    }
  },
  computed : {
      processUrlTrailer(){  
      let result = (this.movie.trailerUrl+"?autoplay=false&width=640").toString()
      console.log(result)   
      return(result)
    }
  }
})
export default class Movie extends Vue {
  msg!: string
}
</script>

