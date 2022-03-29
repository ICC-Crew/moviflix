<template>
    <MenuBar :model="items">
        <template #end>
              <ButtonComp id="login-button" v-on:click="goToLogin()" type="button" label="Connexion" icon="pi pi-user"  />
        </template>
    </MenuBar>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
     
  data() {
		return {
      active:3,
      items: [
                {
                    label: 'Accueil',
                    icon: 'pi pi-home',
                    to: '/'
                },
                {
                    label: 'Films',
                    icon: 'pi pi-video',
                    to: '/movies'
                },
                {
                    label: 'Groupes',
                    icon: 'pi pi-fw pi-users',
                    to: '/login'
                },
            ]
		}
	},
    methods:{
        goToLogin : function(){
            this.$router.push('/login'); 
        }
    },
    computed: {}
})
export default class HeaderComp extends Vue {}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
