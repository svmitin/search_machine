<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import Query from '../components/Query.vue'

const query = ref("IKEA Омск")
</script>

<template>
    <div class="wrapper">
      <Query 
        message="Введи поисковой запрос" 
        :search_text="query" 
      />
    </div>
</template>
