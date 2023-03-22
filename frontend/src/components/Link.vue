<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'


const props = defineProps({
  url: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  },
})

const link = ref('<a href="' + props.url + '">' + props.title + '</a>')
</script>

<template>
<div v-html="link"></div>
</template>

<style scoped>
</style>
