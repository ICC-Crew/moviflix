<template>
    <h1>
        Liste des Films 
    </h1>
    <div class="post">
        <div v-if="loading">
            <ProgressSpinner />
        </div>

        <div v-if="error">{{ error }}</div>

        <div v-if="movieList" >
            <div v-for="movie in movieList" :key="movie._id">
                <h2>{{ movie.title }}</h2>
            </div>
        </div>
    </div>

</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  data() {
    return {
      loading: false,
      movieList: null,
      error: null,
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData: async function(){
      this.error = this.movieList = null
      this.loading = true
 
      
      fetch('http://localhost:3002/API/v1/movies')
        .then(response => {
            if (response.ok){
                return response.json() 
            }      
            throw new Error('Erreur lors de la connection à l API')
        })
        .then(responseJSON =>{
            this.movieList = responseJSON
            this.loading = false
        })
        .catch((error)=>{
            this.error = error.toString()
            console.log(error)
        })
    
    },
  },
})
export default class Movie extends Vue {
  msg!: string
}
</script>


 