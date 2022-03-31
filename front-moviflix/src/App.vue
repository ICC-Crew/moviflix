<template>
<div>
  <HeaderComp class="sticky" />
  <router-view class="min-h-screen"  />
  <FooterComp />
</div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import HeaderComp from '@/components/utils/HeaderComp.vue'; // @ is an alias to /src
import FooterComp from '@/components/utils/FooterComp.vue'

@Options({
  components: {
    HeaderComp,
    FooterComp,
  },
})

export default class App extends Vue {}
</script>


<style>
  body {
      margin: 0;
      height: 100%;
      overflow-x: hidden;
      overflow-y: auto;
      background-color: rgb(0, 0, 0);
      font-family: var(--font-family);
      font-weight: 400;
      color: var(--text-color);
   }
   
   /* The sticky class is added to the navbar with JS when it reaches its scroll position */
.sticky {
  position: fixed;
  top: 0;
  width: 100%;
  z-index:5;
}

/* Add some top padding to the page content to prevent sudden quick movement (as the navigation bar gets a new position at the top of the page (position:fixed and top:0) */
.sticky + .content {
  padding-top: 60px;
}

.main-div{
  margin-left: 20px;
}

.div-text-reinitialize{
  margin-left:auto;
  margin-right:auto;
  width:15%;
  cursor: pointer;
  margin-bottom: 1rem;
}

.div-text-reinitialize:hover{
  color: #ffcd2e;
}

.div-text-register{
  margin-left:auto;
  margin-right:auto;
  width:10%;
  cursor: pointer;
  margin-bottom: 40px;
}

.div-text-register:hover{
  color: #ffcd2e;
}

.justify-center{
  justify-content:center;
  align-items: center;
}

.inscription-button{
  margin-left: 2%;
}


</style>
