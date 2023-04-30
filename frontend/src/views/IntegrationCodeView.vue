<script setup>
import { ref, OnMount } from 'vue'
import { useFetch } from '@vueuse/core'
import { RouterLink } from 'vue-router'
import Query from '../components/Query.vue'
import Response from '../components/Response.vue'

const props = defineProps({
  site_url: {
    type: String,
    required: true
  },
  site_category: {
    type: String,
    required: true
  }
})
const new_metric_code = useFetch('http://api.freedom:8000/register_site').post(
    {
      'url': props.site_url,
      'category': props.site_category
    }
  ).json().data
</script>

<template>
    <div class="wrapper" v-if="new_metric_code && new_metric_code.js_metric_integration_code">

      <p>Сайт добавлен на индексацию. Вот ваш код для интеграции на сайт. Его нужно поместить в блок HEAD каждой страницы сайта</p>
      <p><textarea v-model="new_metric_code.js_metric_integration_code"></textarea></p>
    </div>
</template>

<style scoped>
textarea {
  width: 600px;
  height: 300px;
}
</style>