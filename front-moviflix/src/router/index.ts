import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Movies from '../views/Movies.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Movie from '../components/movies/Movie.vue'
import Recommandation from '../components/movies/Recommandation.vue'
import store from '../store';


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/movies',
    name: 'Movies',
    component: Movies,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  { path: '/movies/:id',
    name:'Movie',
    component: Movie,
    meta: {
        requiresAuth: true
    } 
  },
  { path: '/recommandation',
    name:'Recommandation',
    component: Recommandation,
    meta: {
        requiresAuth: true
    } 
  }

]

function getAuth(){
  return store.getters.isConnected;
}

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const isAuthentificated = getAuth();
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  console.log("auth",isAuthentificated);
  if (requiresAuth && !isAuthentificated){
    next('/login');
  } else {
    next();
  }
});


export default router
