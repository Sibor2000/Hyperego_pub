<template>
    <div class="flex flex-col gap-4 mx-auto p-4" style="min-height: 16rem;">
        <h1 class="text-center mt-4 mb-4 text-xl font-semibold">Subscribe to stay protected</h1>

        <!-- Flex container for subscription options -->
        <div class="flex justify-center gap-4 flex-wrap">
            <Card
            v-for="option in subscriptionOptions"
            :key="option.id"
            style="width: 30%; min-width: 16rem;"
            class="shadow-md transition-transform transform cursor-pointer"
            :class="{
                'hover:scale-105': true,
                'bg-primary-950': selectedOption === option.id,
            }"
            @click.stop="selectOption(option.id)"
            >
            <template #title>
                <h3 class="font-semibold text-lg text-center">{{ option.label }}</h3>
                <p class="text-2xl font-bold text-primary-100 mt-4">{{ option.price }}</p>
            </template>
            <template #subtitle>
                <p class="text-sm text-primary-200 text-center">{{ option.description }}</p>
            </template>
            <template #content>
              <div class="flex flex-col justify-between h-48">
                <p class="m-0 mb-4 text-justify">{{ option.details }}</p>
                <div class="flex justify-center gap-4">
                <Button
                    label="Select Plan"
                    class="w-full"
                    :class="{ 'p-button-primary': selectedOption === option.id }"
                    @click.stop="selectOption(option.id)"
                />
                </div>
                </div>
            </template>
            </Card>
        </div>
  
        <!-- <div class="flex pt-6 justify-center space-x-4">
            <Button label="Subscribe" severity="primary" icon="pi pi-check" @click="subscribe" />
        </div> -->
    </div>
</template>
  
<script setup>
import { ref } from 'vue';
import Button from 'primevue/button';
import Card from 'primevue/card';
import Carousel from 'primevue/carousel';


  // Define subscription options
  const subscriptionOptions = [
    {
        id: 'free_plan',
        label: 'Free Plan',
        price: '$0.00 / Month',
        description: 'Have unlimited access to our custom search feature.',
        details: 'Get unrestricted access to our custom search functionality to explore and monitor your digital blueprint with ease.'
    },
    {
        id: 'pro',
        label: 'Pro Plan',
        price: '$4.99 / Month',
        description: 'Enjoy advanced features for enhanced protection.',
        details: 'In addition to custom search, this plan includes enhanced blueprint detection, deletion and improvement suggestions.'
    },
    {
        id: 'premium',
        label: 'Premium Plan',
        price: '$6.99 / Month',
        description: 'Comprehensive protection and exclusive features.',
        details: 'Includes all features from Premium, plus advanced analytics, dedicated support, and unlimited data storage.'
    }
  ];
  
  // Track selected subscription option
  const selectedOption = ref(null);
  
  // Select an option
  const selectOption = (optionId) => {
    selectedOption.value = optionId;
  };
  
  // Callback functions
  const subscribe = () => {
    if (selectedOption.value) {
      alert(`Subscribed to: ${selectedOption.value}`);
    } else {
      alert('Please select a subscription plan');
    }
  };
  
  const goBack = () => {
    // Trigger the back action (you can modify this based on your needs)
    alert('Going back');
  };
  </script>
  
  <style scoped>
  /* Add any custom styles here */
  .card-footer {
    display: flex;
    justify-content: center;
  }
  </style>
  