import 'primevue/resources/themes/vela-orange/theme.css'       //theme
import 'primevue/resources/primevue.min.css'                 //core css
import 'primeicons/primeicons.css'                           //icons
import '/node_modules/primeflex/primeflex.css'

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import PrimeVue from 'primevue/config';
import Menubar from 'primevue/menubar';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import ProgressBar from 'primevue/progressbar';
import Card from 'primevue/card';
import Paginator from 'primevue/paginator';

const app = createApp(App);
app.use(PrimeVue,{ripple:true});
app.component('MenuBar',Menubar);
app.component('ButtonComp',Button);
app.component('InputText',InputText);
app.component('Password',Password);
app.component('ProgressBar',ProgressBar);
app.component('CardComp',Card);
app.component('PaginatorComp',Paginator);

//app.directive('styleclass', StyleClass); # for animation

app.use(store);
app.use(router);
app.mount('#app');
