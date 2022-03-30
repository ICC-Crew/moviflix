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
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';

const app = createApp(App);

app.use(PrimeVue,{ripple:true});
app.use(ToastService);

app.component('MenuBar',Menubar);
app.component('ButtonComp',Button);
app.component('InputText',InputText);
app.component('Password',Password);
app.component('ToastComp',Toast);


//app.directive('styleclass', StyleClass); # for animation

app.use(store);
app.use(router);
app.mount('#app');
