<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import Link from '../components/Link.vue'

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
    <h3><Link :url=url :title=title /></h3>
    <p><i>{{ description }}</i></p>
    <p>{{ found_with }}</p>
  </div>
</template>

<style scoped>
h3 {
  font-size: 1.2rem;
}
</style>
