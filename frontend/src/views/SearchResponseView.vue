<script setup>
import { ref } from 'vue'
import { useFetch } from '@vueuse/core'
import { RouterLink } from 'vue-router'
import Query from '../components/Query.vue'
import Response from '../components/Response.vue'

const props = defineProps({
  search_text: {
    type: String,
    required: true
  }
})

const query = ref(props.search_text)
// TODO: how use await
const { data } = useFetch('http://api.freedom:8000/search?query='+props.search_text).get().json()
const search_response = data
</script>

<template>
    <div class="wrapper">
      <Query 
        message="Просмотр результатов" 
        :search_text="query" 
      />
      
      <Response 
        v-for="item in search_response.pages"
        v-bind:url="item.url"
        v-bind:title="item.title"
        v-bind:description="item.description"
        v-bind:indexed="item.indexed"
        v-bind:found_with="item.found_with"
      ></Response>
    </div>
</template>

<style scoped>
</style>