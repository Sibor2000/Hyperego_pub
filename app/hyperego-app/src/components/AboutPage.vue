<template>
    <div class="container mx-auto px-4 py-16 mt-4">
      <!-- Hero Section -->
      <section class="text-center mb-24">
        <h1 class="text-5xl font-bold mb-4">About Us</h1>
        <p class="text-xl mb-8">Discover the team behind your digital identity protection</p>
      </section>
  
      <!-- Vision & Mission Section -->
      <section class="mb-24">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
          <Card class="bg-purple-900 text-white">
            <template #header>
              <h2 class="text-3xl font-bold mb-4">Our Vision</h2>
            </template>
            <template #content>
              <p class="text-lg">
                We envision a world where individuals have complete control over their digital identities, 
                empowering them to shape their online presence with confidence and security.
              </p>
            </template>
          </Card>
          <Card class="bg-purple-800 text-white">
            <template #header>
              <h2 class="text-3xl font-bold mb-4">Our Mission</h2>
            </template>
            <template #content>
              <p class="text-lg">
                Our mission is to provide cutting-edge tools and services that enable people to manage, 
                protect, and optimize their digital footprint, ensuring a positive online reputation.
              </p>
            </template>
          </Card>
        </div>
      </section>
  
      <!-- Team Section -->
      <section class="mb-24">
        <h2 class="text-3xl font-bold mb-12 text-center">Meet Our Team</h2>
        <div class="grid grid-cols-1 gap-16">
          <div v-for="(member, index) in teamMembers" :key="member.name" 
               class="flex flex-col md:flex-row items-center"
               :class="{ 'md:flex-row-reverse': index % 2 !== 0 }">
            <div class="w-48 h-48 rounded-full overflow-hidden mb-6 md:mb-0 md:mx-8">
              <img :src="member.photo" :alt="member.name" class="w-full h-full object-cover" />
            </div>
            <div class="text-center md:text-left flex-1" :class="{ 'md:text-right': index % 2 !== 0 }">
              <h3 class="text-2xl font-bold mb-2">{{ member.name }}</h3>
              <h4 class="text-xl text-purple-400 mb-4">{{ member.position }}</h4>
              <p class="text-gray-300">{{ member.bio }}</p>
            </div>
          </div>
        </div>
      </section>
  
      <!-- CTA Section -->
      <section class="text-center">
        <h2 class="text-3xl font-bold mb-4">Ready to Take Control?</h2>
        <p class="text-xl mb-8">Join us in shaping the future of digital identity management.</p>
        <Button label="Get Started Now" icon="pi pi-check" class="p-button-lg" />
      </section>
    </div>
</template>
  
<script setup>
import { ref } from 'vue'
import Card from 'primevue/card'
import Button from 'primevue/button'
const teamMembers = ref([
    {
        name: 'Beke-Szabo Bence',
        position: 'AI Model Developer',
        photo: '/src/assets/bence.png',
        bio: 'Bence specializes in designing and training advanced AI models for predictive analytics and automation. His innovative approach helps drive our cutting-edge solutions for managing digital identities.'
    },
    {
        name: 'Sprencz Robert',
        position: 'Product Designer',
        photo: '/src/assets/robert.png',
        bio: 'Robert crafts impactful marketing strategies that connect with diverse audiences. His expertise ensures our solutions reach those who need them most, empowering individuals to safeguard their digital presence.'
    },
    {
        name: 'Szabo Lorand',
        position: 'Web Maestro',
        photo: '/src/assets/lorand.png',
        bio: 'Lorand is a master of web development, delivering seamless and user-friendly interfaces. He leads the creation of our robust and intuitive platforms that enable users to protect and enhance their online identity.'
    }
])

  </script>
  
  <style scoped>
  .p-card {
    background-color: transparent;
  }
  
  .p-card .p-card-content {
    padding-top: 0;
  }
  </style>
  
  