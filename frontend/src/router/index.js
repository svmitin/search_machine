import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Main',
        component: () =>
            import('../views/SearchMachine.vue'),
    },
    {
        path: '/query',
        name: 'Response',
        component: () =>
            import('../views/Results.vue'),
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
})

export default router
