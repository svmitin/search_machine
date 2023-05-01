<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainView from './views/MainView.vue'
</script>

<template>
  <nav>
    <RouterLink to="/">Главная</RouterLink>
    <RouterLink to="/new_site">Добавить сайт в индекс</RouterLink>
  </nav>
  <RouterView />

  <br><br><br>
  <hr>
  Sergey Mitin © 2023
</template>

<style scoped>
hr {
  width: 250px;
}
</style>
