<template>
    <div class="container mx-auto px-4 py-16 mt-4">
      <!-- Hero Section -->
      <section class="text-center mb-16">
        <h1 class="text-5xl font-bold mb-4">Choose Your Plan</h1>
        <p class="text-xl mb-8">Select the perfect plan to protect your digital identity</p>
      </section>
  
      <!-- Pricing Cards Section -->
      <section class="mb-24">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <Card
            v-for="option in subscriptionOptions"
            :key="option.id"
            class="shadow-lg transition-all duration-300 hover:shadow-2xl"
            :class="{
              'border-4 border-primary-500': selectedOption === option.id,
              'transform hover:-translate-y-2': selectedOption !== option.id
            }"
          >
            <template #header>
              <div class="bg-primary-700 text-white p-4 rounded-t-lg">
                <h2 class="text-2xl font-bold text-center">{{ option.label }}</h2>
              </div>
            </template>
            <template #title>
              <div class="text-center py-4">
                <span class="text-4xl font-bold text-primary-500">{{ option.price }}</span>
                <span class="text-gray-400 ml-2">/ Month</span>
              </div>
            </template>
            <template #content>
              <div class="p-4">
                <p class="text-lg text-center mb-6">{{ option.description }}</p>
                <ul class="space-y-2 mb-8">
                  <li v-for="(feature, index) in option.features" :key="index" class="flex items-center">
                    <i class="pi pi-check-circle text-primary-500 mr-2"></i>
                    <span>{{ feature }}</span>
                  </li>
                </ul>
                <Button 
                    :label="selectedOption === option.id ? 'Selected' : 'Select Plan'"
                    class="w-full p-button-lg"
                    :class="{
                        'p-button-outlined p-button-secondary': selectedOption !== option.id,
                        'p-button-primary': selectedOption === option.id
                    }"
                    @click="selectOption(option.id)"
                />
              </div>
            </template>
          </Card>
        </div>
      </section>
  
      <!-- FAQ Section -->
      <section class="mb-24">
        <h2 class="text-3xl font-bold mb-8 text-center">Frequently Asked Questions</h2>
        <div class="space-y-4">
          <Accordion :multiple="true">
            <AccordionTab v-for="(faq, index) in faqs" :key="index" :header="faq.question">
              <p>{{ faq.answer }}</p>
            </AccordionTab>
          </Accordion>
        </div>
      </section>
  
      <!-- CTA Section -->
      <section class="text-center">
        <h2 class="text-3xl font-bold mb-4">Ready to Secure Your Digital Identity?</h2>
        <p class="text-xl mb-8">Choose your plan and start protecting your online presence today.</p>
        <Button label="Get Started" icon="pi pi-shield" class="p-button-lg" @click="subscribe" />
      </section>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import Card from 'primevue/card';
import Button from 'primevue/button';
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
const subscriptionOptions = [
    {
        id: 'free_plan',
        label: 'Free Plan',
        price: '$0.00 / Month',
        description: 'Have unlimited access to our custom search feature.',
        features: [
            'Unlimited custom search',
        ]
    },
    {
        id: 'pro',
        label: 'Pro Plan',
        price: '$4.99 / Month',
        description: 'Enjoy advanced features for enhanced protection.',
        features: [
            'Enhanced blueprint detection',
            'Deletion suggestions',
            'Priority support'
        ]
    },
    {
        id: 'premium',
        label: 'Premium Plan',
        price: '$6.99 / Month',
        description: 'Comprehensive protection and exclusive features.',
        features: [
            'All Pro Plan features',
            'Advanced analytics',
            'Dedicated support',
            'Unlimited data storage',
            'Improvement recommendations'
        ]
    }
];

  
  const faqs = [
    {
      question: 'What payment methods do you accept?',
      answer: 'We accept all major credit cards, PayPal, and bank transfers for our subscription plans.'
    },
    {
      question: 'Can I upgrade or downgrade my plan?',
      answer: 'Yes, you can upgrade or downgrade your plan at any time. Changes will be reflected in your next billing cycle.'
    },
    {
      question: 'Is there a free trial available?',
      answer: 'We offer a 14-day free trial for our Premium plan. No credit card is required to start your trial.'
    },
    {
      question: 'How secure is my data?',
      answer: 'We use industry-standard encryption and security measures to protect your data. Your privacy and security are our top priorities.'
    }
  ];
  
  const selectedOption = ref(null);
  
  const selectOption = (optionId) => {
    selectedOption.value = optionId;
  };
  
  const subscribe = () => {
    if (selectedOption.value) {
      alert(`Thank you for subscribing to the ${selectedOption.value} plan!`);
    } else {
      alert('Please select a subscription plan before proceeding.');
    }
  };
  </script>
  
  <style scoped>
  .p-card {
    background-color: var(--surface-card);
    color: var(--text-color);
  }
  
  .p-accordion .p-accordion-header .p-accordion-header-link {
    background-color: var(--surface-ground);
    color: var(--text-color);
  }
  
  .p-accordion .p-accordion-content {
    background-color: var(--surface-section);
    color: var(--text-secondary-color);
  }

</style>