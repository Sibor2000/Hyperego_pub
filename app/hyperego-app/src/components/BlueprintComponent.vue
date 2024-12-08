<template>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <Card
      v-for="post in posts"
      :key="post.id"
      class="mt-6"
    >
      <template #header>
        <i v-if="post.source==='Instagram'" class="pi pi-instagram text-4xl mt-4 text-primary-500"></i>
        <i v-if="post.source==='facebook'" class="pi pi-facebook text-4xl mt-4 text-primary-500"></i>
        <i v-if="post.source==='linkedin'" class="pi pi-linkedin text-4xl mt-4 text-primary-500"></i>
        <!-- TODO -->
      </template>

      <template #title class="text-primary-100">
        {{ getTitle(post) }}
      </template>

      <template #content>
        <div>
          <img
            v-if="post.image"
            :src="post.image"
            alt="Post image"
            class="w-full h-64 object-cover rounded-2xl"
          />

          <p class="text-sm text-primary-100 my-2">
            {{ post.content }}
          </p>
          <a :href="post.url" target="_blank">
            <Button label="View Post" icon="pi pi-external-link" />
          </a>

          <!-- Display additional result information -->
          <div class="mt-6">
            <h5 class="text-lg font-semibold">Analysis</h5>

            <div class="mt-2">
              <span v-if="post.verdict" class="font-semibold">Verdict: {{ post.verdict }}</span>
              <Skeleton v-else width="15rem" borderRadius="16px" class="m-auto" />
            </div>

            <div class="flex justify-center mt-2">
              <Rating v-if="post.quality" :model-value="post.quality" readonly class="cursor-default" />
              <Skeleton v-else width="10rem" height="2rem" borderRadius="16px" class="m-auto" />
            </div>

            <div class="flex flex-col gap-2 my-6">
              <p class="font-semibold mb-2">Improvements</p>
              <template v-if="post.improvements">
                <Message v-for="imp in post.improvements" :key="imp" severity="info" class="text-sm">
                  {{ imp }}
                </Message>
              </template>
              <div v-else class="m-auto flex flex-col gap-2">
                <Skeleton width="20rem" height="2rem" borderRadius="8px" />
                <Skeleton width="20rem" height="1.5rem" borderRadius="8px" />
                <Skeleton width="20rem" height="1.5rem" borderRadius="8px" />
              </div>
            </div>
          </div>
        </div>
      </template>
    </Card>
  </div>
</template>

<script setup>
import { computed } from "vue";
import Card from "primevue/card";
import Rating from "primevue/rating";
import Skeleton from "primevue/skeleton";
import Message from "primevue/message";
import Button from "primevue/button";

const props = defineProps({
  messages: {
    type: Array,
    required: true,
  },
});

const posts = computed(() => {
  const scraped = props.messages.filter(
    (message) => message.status === "scraped"
  );
  return scraped.map((message) => {
    let result = props.messages.find(
      (msg) => msg.status === 'result' && msg.result.id === message.post.id
    );
    if (result) {
      return {
        ...message.post,
        ...result.result,
        quality: result.result.quality / 2,
      };
    }
    return { ...message.post };
  });
});

function getTitle(post) {
  let title = `${post.source} Post`;
  title = title.charAt(0).toUpperCase() + title.slice(1);
  return title;
}
</script>

<style scoped>
.pi {
  font-size: 2.5rem;
  padding-top: 4px;
}
</style>