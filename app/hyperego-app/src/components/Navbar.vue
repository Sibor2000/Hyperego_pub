<template>
    <Menubar :model="items" class="z-10 sticky top-0 flex justify-between shadow-xl">
        <template #start class="xd">
            <img src="../assets/logo.png" alt="Logo" class="h-12 my-1 w-auto ml-2 mr-4" />
            <h1 class="text-2xl font-bold mr-8">Hyperego</h1>
        </template>
    </Menubar>
</template>

<script setup>
import { ref } from 'vue'
import Menubar from 'primevue/menubar'
import { useRouter } from 'vue-router';

const router = useRouter();

function navigateToLogin() {
    router.push({ name: 'Login' });
}

function navigateToAbout() {
    router.push({ name: 'AboutPage' });
}

const items = ref([
    {
        label: 'Home',
        icon: 'pi pi-fw pi-home',
        command: () => router.push('/')
    },
    {
        label: 'Custom Search',
        icon: 'pi pi-fw pi-search',
        command: () => router.push('/search')
    },
    {
        label: 'Pricing',
        icon: 'pi pi-fw pi-dollar',
        command: () => router.push('/pricing')
    },
    {
        label: 'About',
        icon: 'pi pi-fw pi-info-circle',
        command: () => router.push('/about')
    },
])
</script>

<style scoped>
:deep(.p-menubar-item .pi) {
  color: var(--primary-400);
}
</style>