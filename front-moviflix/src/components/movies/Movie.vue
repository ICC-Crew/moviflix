<template>
  <h1>
  Film
  </h1>
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
    this.fetchPage()
  },
  methods: {
    goToMovie: function(){
     // this.$router.push('movies/test'); 
    },
    fetchPage : async function(page= 0){
      this.loading = true
      this.error = this.movieList = null
      fetch(`http://localhost:3002/API/v1/movies?limit=20&page=${page}`)
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
            this.loading = false
            console.log(error)
        })
    },
    onPage: function (event:any){
      this.fetchPage(event.page)
    }
  },
})
export default class Movie extends Vue {
  msg!: string
}
</script>

