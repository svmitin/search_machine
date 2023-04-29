import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import SearchResponseView from '../views/SearchResponseView.vue'
import NewSiteView from '../views/NewSiteView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/search/:query', 
      name: 'search-response', 
      component: SearchResponseView,
      props: route => ({ search_text: route.params.query })
    },
    {
      path: '/new_site',
      name: 'new_site',
      component: NewSiteView
    },
  ]
})

export default router
