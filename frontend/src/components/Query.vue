<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'


const props = defineProps({
  search_text: {
    type: String,
    required: true
  }
})
const query = ref(props.search_text)
</script>

<template>
  <div>
    <h3>Введи поисковой запрос</h3>
    <input v-model="query">
    <button @click="$router.push({ name: 'search-response', params: {query: query} })">Найти!</button>
    <p>Поисковой запрос: {{ query }}</p>
  </div>
</template>

<style scoped>
h3 {
  font-size: 1.2rem;
}
</style>
