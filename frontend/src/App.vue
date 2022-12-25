<template>
  <head>
    <meta charset="UTF-8">
    <title>Freedom search</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="icon" type="image/png" href="./assets/favicon.png">
  </head>
  <body>
    <SearchMachine msg="Welcome to Your Vue.js App"/>
  </body>
</template>

<script>
import SearchMachine from './components/SearchMachine.vue'

export default {
  name: 'App',
  components: {
    SearchMachine
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
