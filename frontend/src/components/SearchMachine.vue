<template>
  <div class="SearchMachine" id="search-machine">
    <div class="row g-4 search">
        <h1 v-text="sitename"></h1>
        <input v-model="search_text"><button v-on:click="getResult" class="btn btn-primary">Search!</button>
        result: <h1 v-text="search_response"></h1>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchMachine',
  data() {
    return {
      sitename: 'Freedom Search Machine',
      search_text: 'IKEA Омск',
      search_response: {"id": 1000, "location": "London"}
    }
  },
  props: {
    msg: String
  },
  methods: {
    getResult() {
      fetch('http://api.freedom:8000/search?query=' + this.search_text)
      .then(response => response.json())
      .then(data => (console.log(data)));
      },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.SearchMachine {
  margin-left: auto;
  margin-right: auto;
  width: 800px;
}
</style>
