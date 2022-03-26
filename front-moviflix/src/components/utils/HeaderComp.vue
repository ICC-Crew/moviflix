<template>
<MenuBar :model="items">
</MenuBar>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Shopping from '@/components/cookies/Shopping.vue'
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
                    label: 'Connexion',
                    icon: 'pi pi-fw pi-user',
                    to: '/login'
                }
            ]
		}
	},
    computed: {}
})
export default class HeaderComp extends Vue {}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
