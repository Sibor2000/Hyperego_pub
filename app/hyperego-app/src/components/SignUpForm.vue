<!-- SignUpForm.vue -->
<template>
  <div class="flex flex-col gap-2 mx-auto" style="min-height: auto; max-width: 20rem;">
    <h2 class="text-2xl font-bold text-center text-purple-300 mb-6 mt-4">Enter your data</h2>

    <div class="space-y-4">
      <div class="field">
        <InputText id="input" v-model="name" type="text" placeholder="Name" class="w-full p-inputtext-sm" />
      </div>
      <div class="field">
        <InputText id="email" v-model="email" type="email" placeholder="Email" class="w-full p-inputtext-sm" />
      </div>
      <div class="field">
        <InputText id="profession" v-model="profession" type="text" placeholder="Profession" class="w-full p-inputtext-sm" />
      </div>
      <div class="field">
        <InputText id="age" v-model="age" type="number" placeholder="Age" class="w-full" size="small" />
      </div>
    </div>

    <!-- Social Media Section -->
    <div class="mt-8">
      <h3 class="text-xl font-semibold text-center text-purple-300 mb-4">Social Media Links</h3>
      <div class="grid grid-cols-1 gap-4">
        <div class="space-y-4">
          <div class="flex items-center space-x-2">
            <i class="pi pi-facebook"></i>
            <InputText id="facebook" v-model="facebook" type="url" placeholder="Facebook URL" class="w-full" size="small" />
          </div>
          <div class="flex items-center space-x-2">
            <i class="pi pi-instagram"></i>
            <InputText id="instagram" v-model="instagram" type="url" placeholder="Instagram URL" class="w-full" size="small" />
          </div>
        </div>
        <div class="space-y-4">
          <div class="flex items-center space-x-2">
            <i class="pi pi-linkedin"></i>
            <InputText id="linkedin" v-model="linkedin" type="url" placeholder="LinkedIn URL" class="w-full" size="small" />
          </div>
        </div>
      </div>
    </div>
    <div class="mt-6">
      <Button 
        label="Submit" 
        class="p-button-primary w-full" 
        @click="submitForm" 
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import { useToast } from 'primevue';

const emit = defineEmits(['formResponse']);
const toast = useToast();

const name = ref('Lena Lasconi');
const email = ref('leni@gmail.com');
const age = ref('46');
const profession = ref('plotician');
const facebook = ref(''); //ref('https://www.facebook.com/elenalasconi.romania/');
const instagram = ref('https://www.instagram.com/elenalasconi/?hl=en');
const linkedin = ref(''); //ref('https://www.linkedin.com/in/elenalasconi');


const submitForm = async () => {
  try {
    const response = await fetch('http://localhost:8080/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: name.value,
        age: Number(age.value),
        profession: profession.value,
        instagram: instagram.value,
        facebook: facebook.value,
        linkedin: linkedin.value
      }),
    });

    console.log(response);

    if (!response.ok) {
      throw new Error('Failed to submit.');
    }

    const data = await response.json();

    if (data.success) {
      console.log('Form submitted successfully:', data);
      toast.add({ severity: 'success', summary: 'Success', detail: 'Starting scan!', life: 3000 });
    }else {
      throw new Error(data.details || 'Unexpected error');
    }
    emit('formResponse', data);
  } catch (error) {
    console.error('Error:', error);
    toast.add({ severity: 'error', summary: 'Error', detail: `Could not start scan: ${error.message}`, life: 3000 });
  }
};

</script>

<style scoped>
/* Add any specific styles here */
.p-inputtext {
  padding: 4px;
  padding-left: 16px;
}

.pi {
  color: var(--primary-400);
}
</style>
