<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainView from './views/MainView.vue'
</script>

<template>
  <RouterView />

  <br><br><br>
  <hr width="250px">
  Sergey Mitin © 2023
</template>

<style scoped>

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
