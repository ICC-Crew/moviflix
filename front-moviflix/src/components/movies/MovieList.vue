<template>
    <h1>
      Les Films
    </h1>
      
    <div class="post">
        <PaginatorComp :rows="1" :totalRecords="20" @page="onPage($event)"></PaginatorComp>
        <div v-if="loading">
            <ProgressBar mode="indeterminate" />
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
                  <ButtonComp icon="pi pi-video" label="Infos"/>
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
    }
  },
  created() {
    this.fetchPage()
  },
  methods: {
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


 