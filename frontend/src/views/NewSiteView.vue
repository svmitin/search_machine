<script setup>
import { ref } from 'vue'
import { useFetch } from '@vueuse/core'
import { RouterLink, RouterView } from 'vue-router'

const categories = useFetch('http://api.freedom:8000/get_categories').get().json().data
const site_url = ref('http://api.freedom')
const site_category = ref('')
</script>

<template>
  <div v-if="categories && categories.categories">
    <h3>Введите URL вашего сайта</h3>
    <input v-model="site_url" @keyup.enter="$router.push({ name: 'new_site_integration_code', params: {site_url: site_url, site_category: site_category} })">
    <select v-model="site_category">
      <option v-for="category in categories.categories" v-bind:value="category.id">{{category.category}}</option>
    </select>
    <button @click="$router.push({ name: 'new_site_integration_code', params: {site_url: site_url, site_category: site_category} })">Добавить</button><br><br>

    <p>Ваш сайт будет добавлен в очередь на индексацию. На это может потребоваться некоторое время, но скорее 
    всего он будет проиндексирован за один час. Когда индексация будет завершена, вы сможете найти его в поисковой выдаче.</p>
      
    <ol>Обратите внимание на наш алгоритм ранжирования. Чем больше пунктов вы выполните, тем выше в поисковой выдаче будет ваш сайт:
      <li>Сайт был добавлен на индексацию в поисковую систему через эту форму</li>
      <li>Сайт существует давно</li>
      <li>Сайт не имеет ошибок</li>
      <li>Сайт не имеет банов</li>
      <li>Сайт поддерживает протокол HTTPS</li>
      <li>Сайт подключен к метрике N1</li>
      <li>Сайт является интересным согласно метрике N1</li>
    </ol>
  </div>
</template>

<style scoped>
h3 {
  font-size: 1.2rem;
}
</style>
