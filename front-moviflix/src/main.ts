import 'primevue/resources/themes/vela-orange/theme.css'       //theme
import 'primevue/resources/primevue.min.css'                 //core css
import 'primeicons/primeicons.css'                           //icons
import '/node_modules/primeflex/primeflex.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import PrimeVue from 'primevue/config';
import Menubar from 'primevue/menubar';
import InputText from 'primevue/inputtext';
import Card from 'primevue/card'
import Button from 'primevue/button'
import ChipComp from 'primevue/chip';
import Dialog from 'primevue/dialog';
import Divider from 'primevue/divider';
import Tag from 'primevue/tag';
import Badge from 'primevue/badge';
import ToastService from 'primevue/toastservice';
import Toast from 'primevue/toast';
import StyleClass from 'primevue/styleclass';


const app = createApp(App);
app.use(PrimeVue,{ripple:true});
app.component('MenuBar',Menubar);
//app.component('InputText',InputText);
//app.component('CardComp',Card);
//app.component('ButtonComp',Button);
//app.component('ChipComp',ChipComp);
//app.component('DialogComp',Dialog);
//app.component('DividerComp',Divider);
//app.component('TagComp',Tag);
//app.component('BadgeComp',Badge);
//app.component('ToastComp',Toast);

//app.directive('styleclass', StyleClass); # for animation

//app.use(ToastService)
app.use(store);
app.use(router);
app.mount('#app');
