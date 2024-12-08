<template>
    <div class="container mx-auto px-4 py-8 mt-4">
      <!-- Hero Section -->
      <section class="text-center mb-4">
        <h1 class="text-5xl font-bold mb-4">Custom Search</h1>
        <p class="text-xl mb-4">Tailor your digital footprint search to your specific needs</p>
      </section>
  
      <!-- Search Form Section -->
      <section class="mb-16">
        <Card class="p-4">
          <template #content>
            <form @submit.prevent="startSearch" class="space-y-6">
              <div class="field">
                <label for="name" class="block text-lg font-medium mb-2">Your Name</label>
                <InputText id="name" v-model="name" class="w-full p-inputtext-lg" placeholder="Enter your full name" />
              </div>
  
              <div class="field">
                <label for="desiredTags" class="block text-lg font-medium mb-2">Things You Want to See</label>
                <Chips v-model="desiredTags" class="w-full" placeholder="Enter tags and press enter" />
                <small class="block mt-1 text-gray-400">Enter keywords or phrases you want to include in your search</small>
              </div>
  
              <div class="field">
                <label for="unwantedTags" class="block text-lg font-medium mb-2">Things You Don't Want to See</label>
                <Chips v-model="unwantedTags" class="w-full" placeholder="Enter tags and press enter" />
                <small class="block mt-1 text-gray-400">Enter keywords or phrases you want to exclude from your search</small>
              </div>
  
              <div class="flex justify-center">
                <Button type="submit" label="Start Search" icon="pi pi-search" class="p-button-lg" />
              </div>
            </form>
          </template>
        </Card>
      </section>
  
      <!-- Results Section (placeholder for future implementation) -->
      <section v-if="searchPerformed" class="mb-16">
        <h2 class="text-3xl font-bold mb-8 text-center">Search Results</h2>
        <p class="text-center text-xl">Your custom search results will appear here.</p>
      </section>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import Card from 'primevue/card';
  import InputText from 'primevue/inputtext';
  import Chips from 'primevue/chips';
  import Button from 'primevue/button';
  
  const name = ref('');
  const desiredTags = ref([]);
  const unwantedTags = ref([]);
  const searchPerformed = ref(false);
  
  const startSearch = () => {
    // Placeholder for search functionality
    console.log('Starting search with:', {
      name: name.value,
      desiredTags: desiredTags.value,
      unwantedTags: unwantedTags.value
    });
    
    // Set searchPerformed to true to show the results section
    searchPerformed.value = true;
  
    // Here you would typically make an API call or perform the actual search
    // For now, we'll just log the search parameters
  };
  </script>
  
<style scoped>
.p-card {
    background-color: var(--surface-card);
    color: var(--primary-100);
}

.p-inputtext,
.p-chips .p-inputtext {
    color: var(--primary-200);
    border-color: var(--primary-900);
}

.p-inputtext:focus,
.p-chips .p-inputtext:focus {
    border-color: var(--primary-600);
    box-shadow: 0 0 0 1px var(--primary-600);
}

.p-chips .p-chips-token {
    background-color: var(--primary-600);
    color: var(--primary-200);
}

.p-button {
    background-color: var(--primary-600);
    border-color: var(--primary-600);
}

.p-button:hover {
    background-color: var(--primary-600);
    border-color: var(--primary-600);
}
</style>
  
  