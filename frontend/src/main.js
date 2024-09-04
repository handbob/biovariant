import axios from 'axios'; // Import axios first
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/styles.css'; // Global styles

// Set Axios base URL to point to the backend
axios.defaults.baseURL = 'http://localhost:5001';

const app = createApp(App);
app.use(router);
app.mount('#app');
