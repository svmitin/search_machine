<script setup>
import { ref } from 'vue'
import { useFetch } from '@vueuse/core'
import { RouterLink, RouterView } from 'vue-router'
import Query from '../components/Query.vue'

// TODO: use await
const { data } = useFetch('http://api.freedom:8000/started_query').get().json()
const started_query = data

</script>

<template>
    <div class="wrapper">
      <Query 
        message="Введи поисковой запрос" 
        :search_text="started_query.query" 
      />
    </div>
</template>

<style scoped>
</style>