<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const site_url = ref('')
</script>

<template>
  <div>
    <h3>Введите URL вашего сайта</h3>
    <input v-model="site_url" @keyup.enter="$router.push({ name: 'search-response', params: {query: query} })">
    <select>
      <option>Игры</option>
      <option>Реклама</option>
      <option>Хобби</option>
      <option>Музыка</option>
      <option>Фидео и фильмы</option>
      <option>18+</option>
      <option>Автомобили</option>
      <option>Блоги</option>
      <option>Новости</option>
      <option>Мода и красота</option>
      <option>Здоровье</option>
      <option>Общество</option>
    </select>
    <button @click="$router.push({ name: 'search-response', params: {query: query} })">Добавить</button>

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
