import axios from 'axios'
import App from './App.vue'
import router from './router'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import './assets/styles.css'

axios.defaults.baseURL = 'http://localhost:5001';

const app = createApp(App);

app.use(createPinia())
app.use(router)
app.mount('#app')
