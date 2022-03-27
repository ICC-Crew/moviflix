import { createStore } from 'vuex'

const store = createStore({
    state: {
        movies: [
            {
            "id":0,
            "title":"The Matrix"
            }
        ] 
    },

    getters : {
        movies : (state) => state.movies
    },

    mutations: {},
    actions: {},
    modules: {},


})

export default store;
