<template>
    <h1>
      Les Films
    </h1>
      
    <div class="post">
        <PaginatorComp :rows="1" :totalRecords="numberMovies" @page="onPage($event)" class="m-4"></PaginatorComp>
        <div v-if="loading">
            <ProgressBar mode="indeterminate"/>
        </div>

        <div v-if="error">{{ error }}</div>

        <div v-if="movieList">
        <div class ="flex justify-content-evenly flex-wrap">
            <CardComp class="m-4" v-for="movie in movieList" :key="movie._id" style="width: 18rem">
                <template #header>
                    <img :src="movie.movieCoverUrl" loading="lazy" style="height:25em">
                </template>
                <template #title>
                    {{ movie.title }}
                </template>
                <template #footer>
                  <ButtonComp icon="pi pi-video" label="Infos" @click="goToMovie(movie._id)"/>
                </template>
            </CardComp>
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
      numberMovies:1
    }
  },
  created() {
    this.fetchPage()
  },
  methods: {
    goToMovie: function(movieId:number){
      this.$router.push(`/movies/${movieId}`); 
    },
    fetchPage : async function(page= 0){
      this.loading = true
      this.error = this.movieList = null

      fetch("http://localhost:3002/API/v1/movies/count")
      .then(response => {
            if (response.ok){
                return response.json() 
            }      
            throw new Error('Erreur lors de connecion à l API (compter les films)')
        })
        .then(responseJSON =>{
            this.numberMovies= Number(responseJSON.number)/20
        })
        .catch((error)=>{
            this.error = error.toString()
            console.log(error)
        })
    
      
      fetch(`http://localhost:3002/API/v1/movies?limit=20&page=${page}`)
        .then(response => {
            if (response.ok){
                return response.json() 
            }      
            throw new Error('Erreur lors de la connection à l API (pagination des films) ')
        })
        .then(responseJSON =>{
            this.movieList = responseJSON
            this.loading = false
        })
        .catch((error)=>{
            this.error = error.toString()
            this.loading = false
            console.log(error)
        })
    },
    onPage: function (event:any){
      this.fetchPage(event.page)
    }
  },
})
export default class MovieList extends Vue {
  msg!: string
}
</script>


 