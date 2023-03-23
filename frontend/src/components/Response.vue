<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const props = defineProps({
  url: String,
  title: String,
  description: String,
  indexed: String,
  found_with: String
})
</script>

<template>
  <div>
    <br>
    <h3><a :href='url'>{{ title }}</a></h3>
    <p><i>{{ description }}</i></p>
    <p>{{ found_with }}</p>
  </div>
</template>

<style scoped>
h3 {
  font-size: 1.2rem;
}
</style>
