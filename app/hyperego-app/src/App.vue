<script setup lang="ts">
import { RouterView } from 'vue-router';
import Navbar from './components/Navbar.vue';
import Toast from 'primevue/toast';
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />
    <RouterView />
    <Toast position="bottom-right" />
  </div>
</template>
