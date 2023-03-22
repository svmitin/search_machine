<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import Query from '../components/Query.vue'
import Response from '../components/Response.vue'

const props = defineProps({
  search_text: {
    type: String,
    required: true
  }
})
const query = ref(props.search_text)
const search_response = ref([
  {
    "url": "https://wooordhunt.ru/word/москва", 
    "title": "Москва - перевод на английский, примеры, транскрипция", 
    "description": "Перевод слова 'Москва' на английский - Moscow, Moskva", 
    "indexed": "2023-03-14T19:47:29.419", 
    "found_with": "links search"
  }, 
  {
    "url": "https://wooordhunt.ru/word/\u043c\u043e\u0441\u043a\u0432\u0430", 
    "title": "\u041c\u043e\u0441\u043a\u0432\u0430 - \u043f\u0435\u0440\u0435\u0432\u043e\u0434 \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439, \u043f\u0440\u0438\u043c\u0435\u0440\u044b, \u0442\u0440\u0430\u043d\u0441\u043a\u0440\u0438\u043f\u0446\u0438\u044f.", 
    "description": "\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u0441\u043b\u043e\u0432\u0430 '\u041c\u043e\u0441\u043a\u0432\u0430' \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 - Moscow, Moskva.", 
    "indexed": "2023-03-14T19:47:29.419", 
    "found_with": "full text search"
  }
])
</script>

<template>
    <div class="wrapper">
      <Query 
        message="Просмотр результатов" 
        :search_text="query" 
      />
      <RouterLink to="/">back</RouterLink>
      
      <Response 
        v-for="item in search_response"
        v-bind:url="item.url"
        v-bind:title="item.title"
        v-bind:description="item.description"
        v-bind:indexed="item.indexed"
        v-bind:found_with="item.found_with"
      ></Response>
    </div>
</template>
