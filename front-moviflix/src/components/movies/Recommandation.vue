<template>
  <h1>
  Recommandation Personnalisée
  </h1>
   <div v-if="loading">
            <ProgressBar mode="indeterminate" />
    </div>

    <div v-if="error">{{ error }}</div>

    <div v-if="movie">
        <div class ="flex justify-content-evenly">
        <div>
            <CardComp class="m-4" style="width : 35rem">
                <template #header>
                    <img :src="movie.movieCoverUrl" loading="lazy" >
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
      movie: null,
      error: null,

    }
  },
  created() {
    this.fetchRecommandation(this.$route.params.id)
  },
  methods: {
    goToMovie: function(movieId:number){
      this.$router.push(`/movies/${movieId}`); 
    },

    fetchRecommandation : async function(movieId:string){
      this.loading = true
      this.error = this.movie = null
      let token = this.$store.getters.userToken
      fetch(`http://localhost:3001/API/v1/recommandation/get_recommandation?groupId=6249c6e09ff1623ac50132ab&token=${token}`)
        .then(response => {
            if (response.ok){
                return response.json() 
            }      
            throw new Error('Erreur lors de la connection à l API')
        })
        .then(responseJSON =>{
          setTimeout(() => {
            this.movie = responseJSON
            this.loading = false},300)
        })
        .catch((error)=>{
            this.error = error.toString()
            this.loading = false
            console.log(error)
            this.$router.push('login')
        })
    }
  }
})
export default class Recommandation extends Vue {
  msg!: string
}
</script>

