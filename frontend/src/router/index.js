import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import SearchResponseView from '../views/SearchResponseView.vue'
import NewSiteView from '../views/NewSiteView.vue'
import IntegrationCodeView from '../views/IntegrationCodeView.vue'

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
    {
      path: '/new_site/integration_code/:site_category/:site_url',
      name: 'new_site_integration_code',
      component: IntegrationCodeView,
      props: route => ({ site_url: route.params.site_url, site_category: route.params.site_category })
    },
  ]
})

export default router
