import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import router from './router.js';
import 'primeicons/primeicons.css';


import Aura from '@primevue/themes/aura';
import { definePreset } from '@primevue/themes';
import ToastService from 'primevue/toastservice';

const MyPreset = definePreset(Aura, {
    semantic: {
        primary: {
            50: '{purple.50}',
            100: '{purple.100}',
            200: '{purple.200}',
            300: '{purple.300}',
            400: '{purple.400}',
            500: '{purple.500}',
            600: '{purple.600}',
            700: '{purple.700}',
            800: '{purple.800}',
            900: '{purple.900}',
            950: '{purple.950}'
        }
    }
});

const app = createApp(App);
app.use(PrimeVue, {
    theme: {
        preset: MyPreset,
        options: {
            prefix: 'p',
            darkModeSelector: 'system',
            cssLayer: false
        },
    },
});
app.use(ToastService);
app.use(router);
app.mount('#app');
