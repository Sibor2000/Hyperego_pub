import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from './components/LandingPage.vue';
import AboutPage from './components/AboutPage.vue';
import PricingPage from './components/PricingPage.vue';
import SearchPage from './components/SearchPage.vue';

const routes = [
    { path: '/', component: LandingPage, name: 'LandingPage' },
    { path: '/about', component: AboutPage, name: 'AboutPage' },
    { path: '/pricing', component: PricingPage, name: 'PricingPage' },
    { path: '/search', component: SearchPage, name: 'SearchPage' },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
