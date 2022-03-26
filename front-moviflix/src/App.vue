<template>
<div >
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
</style>
