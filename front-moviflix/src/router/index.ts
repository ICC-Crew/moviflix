import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Movies from '../views/Movies.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Movie from '../components/movies/Movie.vue'


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
    component: Movies
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  { path: '/movies/:id',
    name:'Movie',
    component: Movie },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     if (localStorage.getItem("jwt") == null) {
//       next({
//         path: "/"
//       });
//     } else {
//       next();
//     }
//   } else {
//     next();
//   }
// });


export default router
