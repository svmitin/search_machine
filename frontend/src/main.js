import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import {store} from './store';
import * as components from './components'

createApp(App, router, store).mount('#app')
