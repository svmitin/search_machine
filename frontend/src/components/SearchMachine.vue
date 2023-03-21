<script setup>
import { ref } from 'vue'

defineProps({
  search_text: {
    type: String,
    required: false
  }
})

const a = ref('asdasd')
</script>

<template>
  <div class="SearchMachine">
    <h3>Введи поисковой запрос</h3>
    <input><button class="btn">Найти!</button>
  </div>
  {{ a }}
</template>

<style scoped>
h3 {
  font-size: 1.2rem;
}
</style>
