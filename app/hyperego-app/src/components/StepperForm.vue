<!-- StepperForm.vue -->
<template>
    <section class="mb-16">
      <h2 class="text-3xl font-bold mb-8 text-center">How It Works</h2>
      <Stepper :value="props.initialStep" linear class="max-w-5xl m-auto">
        <StepList>
          <Step v-for="(step, index) in steps" :key="index" :value="index">
            {{ step.label }}
          </Step>
        </StepList>
        <StepPanels>
          <StepPanel v-slot="{ activateCallback }" :value="0" class="bg-transparent">
            <Card class="flex justify-center items-center min-h-[16rem] max-w-xl m-auto">
              <template #content>
                <div class="flex flex-col gap-8">
                <p class="max-w-sm">By allowing us to scan your data, you agree to our Privacy Policy. Your data will remain secure and used only to enhance your digital profile.</p>
                <Button label="Accept" @click="activateCallback(1)" class="px-4 py-2" />
                </div>
              </template>
            </Card>
          </StepPanel>
          <StepPanel v-slot="{ activateCallback }" :value="1" class="bg-transparent!">
            <SignUpForm @formResponse="(response) => handleFormResponse(response, activateCallback)" />
          </StepPanel>
          <StepPanel v-slot="{ activateCallback }" :value="2" class="bg-transparent">
            <div class="flex flex-col justify-center items-center mx-auto" style="min-height: 16rem; max-width: 90%">
                <h1 class="text-center mt-4 text-xl font-semibold">Your Digital Blueprint</h1>
                <div v-if="isLoading" class="flex justify-center items-center min-h-[16rem]">
                    <ProgressSpinner />
                </div>
                <div v-else>
                    <BlueprintComponent :messages="messages" />
                </div>
            </div>
            <div class="flex pt-6 justify-center space-x-4">
              <Button v-show="!isLoading" label="Proceed" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback(3)" />
            </div>
          </StepPanel>
          <StepPanel v-slot="{ activateCallback }" :value="3" class="bg-transparent">
            <SubscriptionForm />
          </StepPanel>
        </StepPanels>
      </Stepper>
    </section>
</template>
  
<script setup>
import { ref, watch } from 'vue';
import Button from 'primevue/button';
import Stepper from 'primevue/stepper';
import StepList from 'primevue/steplist';
import StepPanels from 'primevue/steppanels';
import Step from 'primevue/step';
import StepPanel from 'primevue/steppanel';
import ProgressSpinner from 'primevue/progressspinner';
import Card from 'primevue/card';

import SignUpForm from './SignUpForm.vue';

import SubscriptionForm from './SubscriptionForm.vue';
import BlueprintComponent from './BlueprintComponent.vue';

const steps = ref([
{ label: 'Consent', icon: 'pi pi-user-plus' },
{ label: 'Scan', icon: 'pi pi-search' },
{ label: 'Review', icon: 'pi pi-list' },
{ label: 'Erase Data', icon: 'pi pi-trash' },
]);

const props = defineProps({
    initialStep: {
        type: Number,
        default: 0,
    },
});

watch(() => props.initialStep, (newStep) => {
    console.log('New step:', newStep);
});

const formResponse = ref(null);

const messages = ref([]);
const isLoading = ref(true);

let ws = null;

const handleFormResponse = (response, activateCallback) => {
    formResponse.value = response;
    console.log('Received token:', formResponse.value);
    if (!formResponse.value.success) {
        alert("Could not perform operation");
    } else {
        ws = new WebSocket('ws://localhost:8080/ws');
        
        ws.onopen = () => {
            console.log('WebSocket connection established');
            ws.send(JSON.stringify({
                token: formResponse.value.token
            }));
        };

        ws.onmessage = (event) => {
            const message = JSON.parse(event.data);
            messages.value.push(message);
            console.log('Received message from WebSocket server:', message);

            if (message.status !== 'started') {
                isLoading.value = false;
            }
        };

        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        ws.onclose = () => {
            console.log('WebSocket connection closed');
        };

        activateCallback(2);
    }
};

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
  