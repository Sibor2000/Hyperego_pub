<template>
    <div class="container mx-auto px-4 py-16 mt-4">
        <!-- Hero Section -->
        <section class="text-center mb-24">
            <div class="flex flex-col gap-4 my-16">
            <h1 class="text-5xl font-bold mb-4">Take Control of Your Digital Identity</h1>
            <p class="text-xl mb-8">Discover how the world sees you online, refine your digital presence, and safeguard your future.</p>
            </div>
            <div class="flex gap-4 justify-center">
                <Button label="Try For Free" icon="pi pi-arrow-right" iconPos="right" size="large" @click="getStarted" />
                <Button label="Learn More" size="large" severity="secondary" />
            </div>
             
        </section>

        <section class="flex flex-col items-start gap-4 my-16">
            <h2 class="text-3xl">Your Online Presence, Perfected.</h2>
            <p class="text-left text-lg">In today's digital age, your reputation is your résumé. Whether you're applying for jobs, networking, or just living your life, you deserve a digital profile that reflects the best version of you.</p>
        </section>

        <!-- Features Section -->
        <section class="mb-16 mt-36">
            <h2 class="text-3xl font-bold mb-12 text-center">Key Features</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <Card v-for="feature in features" :key="feature.title" class="py-10">
                    <template #header>
                        <div :class="feature.icon" class="text-8xl mb-4 mt-8 border rounded-full p-4 text-purple-400 border-gray-700"></div>
                    </template>
                    <template #title>
                        {{ feature.title }}
                    </template>
                    <template #content>
                        <p class="text-gray-200">{{ feature.description }}</p>
                    </template>
                </Card>
            </div>
        </section>

        <section id="stepper-form" class="mt-36">
            <StepperForm :initialStep="activeStep"/>
        </section>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import Button from 'primevue/button'
import Card from 'primevue/card'
import { useRouter } from 'vue-router';

import StepperForm from './StepperForm.vue';


const router = useRouter();

const features = ref([
    {
        icon: 'pi pi-search',
        title: 'Comprehensive Scan',
        description: 'Our advanced algorithms scan the web to locate all traces of your digital presence.'
    },
    {
        icon: 'pi pi-trash',
        title: 'Data Removal',
        description: 'We securely remove your personal information from various online platforms and databases.'
    },
    {
        icon: 'pi pi-shield',
        title: 'Privacy Protection',
        description: 'Ongoing monitoring and protection to prevent future data leaks and privacy breaches.'
    }
])

const steps = ref([
    { label: 'Sign Up', icon: 'pi pi-user-plus' },
    { label: 'Scan Your Presence', icon: 'pi pi-search' },
    { label: 'Review Findings', icon: 'pi pi-list' },
    { label: 'Erase Data', icon: 'pi pi-trash' },
    { label: 'Stay Protected', icon: 'pi pi-shield' }
])

const activeStep = ref(0);

function getStarted() {
    // activeStep.value = 1;

    const stepperFormElement = document.getElementById('stepper-form');
    if (stepperFormElement) {
        stepperFormElement.scrollIntoView({ behavior: 'smooth' });
    }
}

</script>

<style scoped>
.p-stepper .p-step {
    background: transparent;
}

.p-stepper .p-step-panel {
    background: transparent;
}

.p-stepper .p-step-panels {
    background: transparent;
}
</style>