import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import SearchResponseView from '../views/SearchResponseView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView},
    {
      path: '/search/:query', 
      name: 'search-response', 
      component: SearchResponseView,
      props: route => ({ search_text: route.params.query })
    },
  ]
})

export default router
