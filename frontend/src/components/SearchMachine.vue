<script setup>
defineProps({
  search_text: {
    type: String,
    required: false
  }
})
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ search_text }}</h1>
    <h3>Введи поисковой запрос</h3>
    <input><button class="btn btn-primary">Найти!</button>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
