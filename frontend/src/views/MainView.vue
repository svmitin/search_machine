<script setup>
import { ref } from 'vue'
import { useFetch } from '@vueuse/core'
import { RouterLink, RouterView } from 'vue-router'
import Query from '../components/Query.vue'

const { data } = useFetch('http://api.freedom:8000/started_query').get().json()
const started_query = data
</script>

<template>
    <div class="wrapper" v-if="started_query && started_query.query">
      <Query 
        message="Введи поисковой запрос" 
        :search_text="started_query.query" 
      />
    </div>
</template>

<style scoped>
</style>