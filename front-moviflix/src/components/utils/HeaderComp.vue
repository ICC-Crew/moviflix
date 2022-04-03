<template>
    <MenuBar :model="items">
        <template #end>
              <ButtonComp v-if="!isConnected" id="login-button" v-on:click="goToLogin()" type="button" label="Connexion" icon="pi pi-sign-in" />
              <ButtonComp v-if="isConnected" class="p-button-danger" id="logout-button" v-on:click="logout()" type="button" label="Deconnexion" icon="pi pi-sign-out" />
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
                    label: 'Recommandation',
                    icon: 'pi pi-fw pi-users',
                    to: '/recommandation'
                },
            ]
		}
	},
    methods:{
        removeToken : function(){
            this.$store.dispatch("removeToken")
            this.$store.dispatch("disconnect")
        },
        goToLogin : function(){
            this.$router.push('/login'); 
        },
        logout : function(){
            this.$store.dispatch("disconnect")
            this.goToLogin()
        }
    },
    computed: {
        isConnected(){
            return this.$store.getters.isConnected
        }
    }
})
export default class HeaderComp extends Vue {}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
