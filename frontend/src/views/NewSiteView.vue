<script setup>
import { ref } from 'vue'
import { useFetch } from '@vueuse/core'
import { RouterLink, RouterView } from 'vue-router'

const site_url = ref('')
const site_category = ref('')

function register_site_and_get_integration_code(params) {
  const { data } = useFetch('http://api.freedom:8000/add_site').post(
    {
      'site_url': site_url.value,
      'site_category': site_category.value
    }
  ).json()
  alert('Сайт добавлен на индексацию. Вот ваш код для интеграции на сайт. Его нужно поместить в блок HEAD каждой страницы сайта')
}

</script>

<template>
  <div>
    <h3>Введите URL вашего сайта</h3>
    <input v-model="site_url" @keyup.enter="register_site_and_get_integration_code()">
    <select v-model="site_category">
      <option value="games">Игры</option>
      <option value="ad">Реклама</option>
      <option value="hobby">Хобби</option>
      <option value="music">Музыка</option>
      <option value="movies">Фидео и фильмы</option>
      <option value="18+">18+</option>
      <option value="auto">Автомобили</option>
      <option value="blogs">Блоги</option>
      <option value="news">Новости</option>
      <option value="beauty">Мода и красота</option>
      <option value="health">Здоровье</option>
      <option value="social">Общество</option>
      <option value="shops">Магазины</option>
    </select>
    <button @click="register_site_and_get_integration_code()">Добавить</button>

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
