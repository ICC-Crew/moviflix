import { createStore } from 'vuex'

const store = createStore({
    state: {
        movies: [
            {
            "id":0,
            "title":"The Matrix"
            }
        ],
        userToken: "" ,
        isConnected : false
    },

    getters : {
        movies : (state) => state.movies,
        userToken : (state) => state.userToken,
        isConnected : (state) => state.isConnected
    },

    mutations: {
        ADD_token(state, token){
            state.userToken = token;
        },
        REMOVE_token(state){
            state.userToken = "";
        },
        CONNECT_status(state){
            state.isConnected = true
        },
        DISCONNECT_status(state){
            state.isConnected = false
        }
    },
    actions: {
        addToken(context, token){
            context.commit("ADD_token", token);
        },
        removeToken(context){
            context.commit("REMOVE_token");
        },
        connect(context){
            context.commit("CONNECT_status")
        },
        disconnect(context){
            context.commit("DISCONNECT_status")
        }

    },
    modules: {},


})

export default store;
